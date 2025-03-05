(Copia y guarda como `informe.md`)**
```markdown
# 📑 Informe del Análisis de Datos Bancarios

## 1️⃣ Introducción
Este informe documenta el análisis de un conjunto de datos bancarios con el objetivo de identificar factores clave que afectan la suscripción a un producto financiero.

## 2️⃣ Cambios Realizados en los Datos

### 📌 Columnas Eliminadas
Se eliminaron/modificaron columnas irrelevantes o redundantes del dataset original:

['day_of_week', ‘date’, 'day_name', 'contact', 'poutcome']

## 📌 Motivos de la Eliminación  

- **`day_of_week`**, **`date`** y **`day_name`** no aportaban valor en el análisis.  
- La columna original era **`date`**, que posteriormente fue separada en distintas fechas creyendo que mejoraría el análisis.  
- Sin embargo, al combinar el dataset con el archivo de Excel, se obtuvo otra fecha adicional, por lo que se optó por recuperar la columna original **`date`** y renombrarla.  
- **`contact`** y **`poutcome`** se transformaron en nuevas variables más útiles.  

---

## 📌 Columnas Agregadas o Modificadas  

Se añadieron nuevas variables para enriquecer el análisis:
['dias_desde_registro', 'categoria_duracion', 'tiene_hipoteca', 'tipo_contacto_modificado']

### Descripción de las nuevas columnas: 

- **`dias_desde_registro`** → Días entre el registro y el contacto con el cliente. 
- **`categoria_duracion`** → Clasifica las llamadas en "Corta", "Media" o "Larga". 
- **`tiene_hipoteca`** → Variable categórica de si el cliente tiene hipoteca o no. 
- **`tipo_contacto_modificado`** → Variación del tipo de contacto con el cliente. 

--- 

## 📌 Manejo de Valores Nulos Antes de la limpieza, el dataset contenía valores nulos en variables clave:

ocupacion: 288
educacion: 1731
dias_ultimo_contacto: 39673

### Tras el proceso de limpieza: 

- 🔹 Se eliminaron los **NaN críticos** en `ocupacion` y `educacion`. 
- 🔹 Se imputaron valores en **`dias_ultimo_contacto`** usando la **mediana**. 
✔ Se eliminaron columnas innecesarias. 
✔ Se imputaron valores nulos con la mediana en variables numéricas. ✔ Se eliminaron registros con datos críticos faltantes. 
✔ Se crearon nuevas variables derivadas. 

---

## 3️⃣ Análisis Exploratorio y Visualizaciones 

### 📊 1. Distribución de la Duración de Llamadas 

- Se observa que la mayoría de las llamadas tienen una **duración corta**. 
- Existen algunas llamadas muy largas, pero son menos frecuentes. 

### 📊 2. Distribución del Ingreso de los Clientes 

- Se observa una **alta dispersión en los ingresos**. 
- Es posible que clientes con **ingresos más altos** tengan comportamientos diferentes. 

### 📊 3. Relación entre Duración de Llamada y Suscripción 

- **Clientes con llamadas más largas tienen mayor probabilidad de suscribirse.** 
- Se confirma que la **duración de la llamada influye en la conversión**. 

### 📊 4. Matriz de Correlaciones entre Variables Claves 

- Se analizó la relación entre **`duracion_llamada`**, **`ingreso`**, **`tasa_empleo`** y **`suscribio`**. 
- Se encontraron **correlaciones relevantes** que pueden ayudar en futuras estrategias de negocio.  
# 📊 Análisis Exploratorio de Datos (EDA) - Banco Portugués

Después de un análisis exhaustivo del dataset proporcionado por un **banco portugués**, hemos identificado patrones clave que influyen en la tasa de conversión de clientes hacia la contratación de productos financieros.

---

## 🔹 **1. Factores Clave en la Conversión de Clientes**

### 🕒 **Duración de la Llamada: Un Factor Decisivo**
- Existe una **correlación positiva fuerte** entre la duración de la llamada y la tasa de conversión.
- **Llamadas cortas (<100 segundos)** tienen una baja tasa de conversión.
- **Llamadas largas (>300 segundos)** aumentan significativamente la conversión.
- Se recomienda mejorar los guiones de venta para mantener conversaciones más largas y efectivas.

### 💰 **Impacto del Ingreso y la Ocupación**
- **Los clientes con mayores ingresos y posiciones laborales más altas** (profesionales, administrativos, gerentes) tienen mayor tasa de conversión.
- Se recomienda realizar campañas segmentadas en función del perfil socioeconómico.

### 🏡 **Estado Civil y Educación: Influencia en la Suscripción**
- **Clientes casados** muestran una mayor tasa de conversión que solteros o divorciados.
- **Personas con educación universitaria** tienden a contratar productos financieros con más frecuencia.
- Esto sugiere que la estabilidad familiar y el nivel educativo influyen en la toma de decisiones financieras.

---

## 🔹 **2. Impacto de Variables Económicas**

### 📈 **Factores Macroeconómicos y su Relación con la Conversión**
- Se observó que la **tasa de empleo**, la **confianza del consumidor** y la **tasa de interés (euribor3m)** afectan la decisión de los clientes.
- **Cuando la tasa de empleo es alta y la confianza del consumidor es positiva**, más clientes están dispuestos a invertir.
- **Cuando la tasa de interés euribor3m es alta**, la conversión baja, posiblemente porque los clientes perciben condiciones de crédito menos favorables.
- Se recomienda ajustar las campañas en función del contexto económico.

### 📊 **Correlaciones Clave Entre Variables**
- La duración de la llamada, el ingreso y la confianza del consumidor están correlacionados con la conversión.
- Se recomienda ejecutar campañas más agresivas cuando las condiciones económicas son favorables.

---

## 🔹 **3. Evolución de la Tasa de Conversión en el Tiempo**

### 📅 **Patrones Temporales en la Conversión**
- La tasa de conversión varía mes a mes, indicando un posible **patrón estacional**.
- Se recomienda ajustar las estrategias de marketing en función de los meses de mayor conversión.

---

## 🔹 **4. Relación Entre Visitas Web y Suscripción**

### 🌐 **Actividad Online y Conversión**
- **Clientes que visitan más veces la web del banco tienen una mayor tasa de conversión.**
- El análisis muestra que aquellos con **frecuencia de visitas más alta** son más propensos a aceptar la oferta.
- Se recomienda reforzar estrategias de retargeting y personalización en la web para aumentar la conversión.

---

## 🔹 **5. Decisión de Eliminar las Columnas de Latitud y Longitud**

Dado que el banco analizado es **portugués** y la segmentación de clientes **no se basa en ubicaciones específicas dentro del país**, se ha decidido **eliminar las columnas de latitud y longitud** del dataset.

### 📌 **Razones para esta decisión**:
❌ **No se encontraron patrones geográficos relevantes en la conversión**.  
❌ **Las estrategias del banco no están enfocadas en segmentación geográfica dentro de Portugal**.  
❌ **Reducimos el tamaño del dataset y mejoramos la eficiencia del análisis eliminando información redundante**.  

💡 **Si en el futuro se plantea una estrategia de marketing geolocalizada, se podría reconsiderar el uso de estas variables**.

---

## 🚀 **Conclusiones Finales y Recomendaciones**

1️⃣ **Optimizar la duración de las llamadas** para aumentar la tasa de conversión.  
2️⃣ **Segmentar campañas según ingresos, ocupación y educación** para mejorar la efectividad.  
3️⃣ **Aprovechar datos macroeconómicos** para ajustar estrategias en función del contexto financiero.  
4️⃣ **Ajustar campañas a patrones estacionales** para aprovechar los meses con mayor conversión.  
5️⃣ **Fortalecer estrategias digitales y retargeting** para captar clientes con alta actividad en la web.

📌 **Conclusión Final:**  
Este análisis ha permitido identificar **factores clave** que impactan la conversión de clientes en campañas bancarias en Portugal. Con estrategias basadas en estos insights, es posible **mejorar significativamente la efectividad de futuras campañas de marketing y ventas**. 🚀📊  
### **Autor y Agradecimientos**

* **Autor:** Ana Nieto Carrera  
* **Datos Inspirados:** Proyecto de base de datos dado por la plataforma.