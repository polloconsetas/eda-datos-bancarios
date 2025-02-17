import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 1. Función para cargar datos con manejo de errores
def cargar_datos(ruta_csv):
    """
    Carga el dataset desde un archivo CSV.
    """
    try:
        df = pd.read_csv(ruta_csv)
        print("✅ Datos cargados correctamente.")
        return df
    except FileNotFoundError:
        print("❌ Error: Archivo no encontrado.")
        return None

# 📌 2. Función para limpiar datos
def limpiar_datos(df):
    """
    Realiza limpieza del dataset:
    - Elimina columnas innecesarias.
    - Traduce nombres de columnas.
    - Optimiza tipos de datos.
    - Maneja valores NaN correctamente.
    """
    columnas_a_eliminar = ['day_of_week', 'day_name', 'year', 'month', 'day', 'latitud', 'longitud']
    df.drop(columns=columnas_a_eliminar, inplace=True, errors='ignore')

    # Ajuste de nombres de columnas a snake_case
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Diccionario para traducir nombres de columnas
    columnas_traducidas = {
        "job": "ocupacion", "marital": "estado_civil", "education": "educacion",
        "housing": "tiene_hipoteca", "loan": "tiene_prestamo", "contact": "tipo_contacto",
        "duration": "duracion_llamada", "campaign": "contactos_actuales",
        "pdays": "dias_ultimo_contacto", "previous": "contactos_previos",
        "poutcome": "resultado_campana_anterior", "emp_var_rate": "tasa_empleo",
        "cons_price_idx": "indice_precio_consumidor", "cons_conf_idx": "indice_confianza_consumidor",
        "euribor3m": "tasa_interes_3m", "nr_employed": "num_empleados",
        "y": "suscribio", "income": "ingreso", "kidhome": "hijos_ninos",
        "teenhome": "hijos_adolescentes", "dt_customer": "fecha_registro",
        "numwebvisitsmonth": "visitas_web_mes", "pdays_category": "categoria_dias_ultimo_contacto",
        "year_registered": "ano_registro", "month_registered": "mes_registro",
        "contact_date": "fecha_contacto"
    }

    df.rename(columns=columnas_traducidas, inplace=True)

    # Optimizar tipos de datos
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'], errors='coerce')
    df['fecha_contacto'] = pd.to_datetime(df['fecha_contacto'], errors='coerce')

    # Convertir variables categóricas a category para optimización
    categorias = ["estado_civil", "educacion", "ocupacion", "tipo_contacto", "resultado_campana_anterior"]
    for col in categorias:
        if col in df.columns:
            df[col] = df[col].astype('category')

    # Manejo de valores NaN
    df.dropna(subset=['ocupacion', 'estado_civil', 'educacion'], inplace=True)
    df.fillna(df.median(numeric_only=True), inplace=True)

    print("✅ Datos limpiados y optimizados correctamente. (Columnas de latitud y longitud eliminadas)")
    return df

# 📌 3. Función para transformar datos
def transformar_datos(df):
    """
    Realiza transformaciones:
    - Calcula 'dias_desde_registro'.
    - Categoriza la duración de la llamada.
    """
    df['dias_desde_registro'] = (df['fecha_contacto'] - df['fecha_registro']).dt.days

    # Categorizar la duración de la llamada
    df['categoria_duracion'] = pd.cut(
        df['duracion_llamada'],
        bins=[0, 100, 300, float('inf')],
        labels=['Corta', 'Media', 'Larga'],
        right=False
    )

    print("✅ Transformaciones aplicadas correctamente.")
    return df

# 📌 4. Función para generar visualizaciones
def generar_visualizaciones(df):
    """
    Genera gráficos clave para el análisis exploratorio.
    """

    # 📊 1. Gráfico de Barras - Duración de Llamada vs. Suscripción
    plt.figure(figsize=(10,6))
    sns.countplot(x=df['categoria_duracion'], hue=df['suscribio'], palette=["red", "blue"])
    plt.xlabel("Categoría de Duración de Llamada")
    plt.ylabel("Cantidad de Clientes")
    plt.title("Categoría de Duración de Llamada según Suscripción")
    plt.legend(title="Suscribió", labels=["No", "Sí"])
    plt.show()

    # 📊 2. Distribución de Edad
    plt.figure(figsize=(10,6))
    sns.histplot(df['age'], bins=30, kde=True, color='blue')
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.title("Distribución de la Edad de los Clientes")
    plt.show()

    # 📊 3. Tasa de Conversión por Estado Civil y Educación
    conversion_estado_civil = df.groupby('estado_civil', observed=True)['suscribio'].mean().reset_index()
    conversion_estado_civil['suscribio'] *= 100  

    conversion_educacion = df.groupby('educacion', observed=True)['suscribio'].mean().reset_index()
    conversion_educacion['suscribio'] *= 100

    plt.figure(figsize=(12,6))
    sns.barplot(data=conversion_estado_civil, x='estado_civil', y='suscribio')
    plt.xlabel("Estado Civil")
    plt.ylabel("Tasa de Conversión (%)")
    plt.title("Tasa de Conversión por Estado Civil")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(12,6))
    sns.barplot(data=conversion_educacion, x='educacion', y='suscribio')
    plt.xlabel("Nivel Educativo")
    plt.ylabel("Tasa de Conversión (%)")
    plt.title("Tasa de Conversión por Nivel Educativo")
    plt.xticks(rotation=45)
    plt.show()

    # 📊 4. Evolución de la Tasa de Conversión por Año y Mes
    df['ano_mes_contacto'] = df['fecha_contacto'].dt.to_period('M').astype(str)  
    conversion_por_mes = df.groupby('ano_mes_contacto')['suscribio'].mean() * 100  

    plt.figure(figsize=(14,6))
    plt.plot(conversion_por_mes.index, conversion_por_mes.values, marker='o', linestyle='-', color='blue', label="Tasa de Conversión")
    plt.xlabel("Fecha (Año-Mes)")
    plt.ylabel("Tasa de Conversión (%)")
    plt.title("Evolución de la Tasa de Conversión por Año y Mes")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.show()

# 📌 5. Ejecutar el script
if __name__ == "__main__":
    ruta_csv = "dataset_final.csv"  # Cambia la ruta si es necesario


    df = cargar_datos(ruta_csv)

    if df is not None:
        df = limpiar_datos(df)
        df = transformar_datos(df)

        # Guardar dataset optimizado
        df.to_csv("dataset_final.csv", index=False)
        print("✅ Dataset final guardado como 'dataset_final.csv'.")

        # Generar visualizaciones
        generar_visualizaciones(df)
