import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# 📌 1. Función para cargar datos
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
    columnas_a_eliminar = ['day_of_week', 'day_name', 'year', 'month', 'day']
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

    # Convertir a fechas
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'], errors='coerce')
    df['fecha_contacto'] = pd.to_datetime(df['fecha_contacto'], errors='coerce')

    # Eliminar valores NaN en columnas clave
    df.dropna(subset=['ocupacion', 'estado_civil', 'educacion'], inplace=True)

    # Imputar valores numéricos con la mediana
    df.fillna(df.median(numeric_only=True), inplace=True)

    print("✅ Datos limpiados y optimizados correctamente.")
    return df

# 📌 3. Función para transformar datos
def transformar_datos(df):
    """
    Realiza transformaciones:
    - Calcula 'dias_desde_registro'.
    - Categoriza la duración de la llamada.
    """
    df = df.dropna(subset=['fecha_contacto', 'fecha_registro'])
    df['dias_desde_registro'] = (df['fecha_contacto'] - df['fecha_registro']).dt.days

    df['duracion_llamada'].fillna(df['duracion_llamada'].median(), inplace=True)

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
    import pandas as pd
import folium
from folium.plugins import MarkerCluster

# 📌 Cargar el dataset
file_path = "/mnt/data/dataset_final.csv"
df = pd.read_csv(file_path)

# 📌 Verificar si las columnas de latitud y longitud existen
if 'latitud' not in df.columns or 'longitud' not in df.columns:
    raise ValueError("❌ Error: No se encontraron las columnas de latitud y longitud en el dataset.")

# 📌 Crear un mapa base centrado en la ubicación promedio de los clientes
map_center = [df['latitud'].mean(), df['longitud'].mean()]
m = folium.Map(location=map_center, zoom_start=6)

# 📌 Crear un clúster de marcadores
marker_cluster = MarkerCluster().add_to(m)

# 📌 Agregar puntos al mapa con colores según suscripción
for _, row in df.iterrows():
    folium.Marker(
        location=[row['latitud'], row['longitud']],
        popup=f"Cliente ID: {row['id']}\nSuscribió: {'Sí' if row['suscribio'] == 1 else 'No'}",
        icon=folium.Icon(color="blue" if row['suscribio'] == 1 else "red")
    ).add_to(marker_cluster)

# 📌 Guardar el mapa interactivo
map_path = "/mnt/data/mapa_clientes.html"
m.save(map_path)

# 📌 Devolver la ruta del archivo generado
map_path

    # 📊 1. Distribución de la Duración de Llamadas
plt.figure(figsize=(10,6))
sns.histplot(df['duracion_llamada'], bins=30, kde=True, color="blue")
plt.xlabel("Duración de la Llamada (segundos)")
plt.ylabel("Frecuencia")
plt.title("Distribución de la Duración de Llamadas")
plt.show()

    # 📊 2. Distribución del Ingreso
plt.figure(figsize=(10,6))
sns.histplot(df['ingreso'], bins=30, kde=True, color="green")
 plt.xlabel("Ingreso Anual")
    plt.ylabel("Frecuencia")
    plt.title("Distribución de los Ingresos de los Clientes")
    plt.show()

    # 📊 3. Relación entre Duración de Llamada y Suscripción
    plt.figure(figsize=(10,6))
    sns.boxplot(x=df['suscribio'], y=df['duracion_llamada'])
    plt.xlabel("Suscribió (0=No, 1=Sí)")
    plt.ylabel("Duración de la Llamada (segundos)")
    plt.title("Duración de la Llamada según Suscripción")
    plt.show()

    # 📊 4. Matriz de Correlaciones con Variables Claves
    columnas_interes = ['duracion_llamada', 'ingreso', 'tasa_empleo', 'suscribio']
    plt.figure(figsize=(12,8))
    sns.heatmap(df[columnas_interes].corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Matriz de Correlaciones entre Variables Claves")
    plt.show()

# 📌 5. Ejecutar el script
if __name__ == "__main__":
    df = cargar_datos("dataset_final.csv")
    if df is not None:
        df = limpiar_datos(df)
        df = transformar_datos(df)
        df.to_csv("dataset_final_procesado.csv", index=False)
        generar_visualizaciones(df)
