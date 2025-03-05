# Proyecto de Análisis de Datos Bancarios 📊
## 📌 Descripción del Proyecto
Este proyecto tiene como objetivo analizar datos bancarios para entender los factores que influyen en la suscripción a un producto financiero. Se realiza un análisis exploratorio, limpieza y transformación de datos, junto con visualizaciones clave para extraer insights.

## 📂 Estructura del Proyecto
- `bank-additional.csv` → Dataset original sin procesar.
- `dataset_final.csv` → Archivo con los datos finales procesados.
- `customer-details.xlsx` → Datos adicionales utilizados en el análisis.
- `limpieza.py` → Script de Python para limpiar, transformar y visualizar los datos.
- `README.md` → Documentación general del proyecto.
- `informe.md` → Explicación detallada del análisis realizado.

## 📊 Visualizaciones Incluidas
- Distribución de la Duración de Llamadas
- Distribución del Ingreso de los Clientes
- Relación entre Duración de Llamada y Suscripción
- Matriz de Correlaciones entre Variables Claves

## 📌 Conclusiones Clave
✔ La duración de la llamada tiene una relación con la suscripción.
✔ Los ingresos de los clientes presentan una distribución variada.
✔ Algunas variables tienen correlaciones significativas con la conversión.

## 🛠️ Instalación y Requisitos
Para ejecutar este proyecto, necesitas tener **Python 3.x** y las siguientes bibliotecas:

```bash
pip install pandas numpy matplotlib seaborn openpyxl

🚀 Ejecución del Script
Para ejecutar el análisis y generar las visualizaciones:
bash

python limpieza.py

Esto cargará los datos, realizará la limpieza y transformación, y generará las visualizaciones correspondientes.
