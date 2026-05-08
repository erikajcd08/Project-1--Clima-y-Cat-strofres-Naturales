# Project-1--Clima-y-Cat-strofres-Naturales
# Proyecto 1: Clima y Catástofres Naturales

## Introducciñon del proyecto

El objetivo de este proyecto es analizar los datos entre el cambio climático y los desastres naturales a nivel global, comparando las tendencias por continente y región entre los años 1900 y 2021.

---

## Dataset

- **Fuente 1:** EM-DAT- All Natural Disasters 1900- 2021 de Kaggle:
        -- 16.701 registros de desastres naturales a nivel global
        -- Link del dataset: https://www.kaggle.com/datasets/brsdincer/all-natural-disasters-19002021-eosdis
- **Fuente 2:** **Temperaturas históricas**:
        -- [Open-Meteo Archive API](https://archive-api.open-meteo.com)
        -- API gratuita de datos climáticos históricos
        -- 27 ciudades de todos los continentes (1950-2021)

---

# Hipótesis
- 1. Los desastres naturales han aumentado progresivamente desde 1900.
- 2. Las regiones más cálidas registran más desastres naturales.
- 3. Asia y América concentran el mayor número de desastres.

---

### Variables principales:
- `Year` → Año del desastre  
- `Disaster Type` → Tipo de desastre (Inundación, terremoto, tormentas...)  
- `Continent` → Continente donde ocurrió el desastre  
- `Region` → Región específica  
- `Country` → País afectado  
- `Total Deaths` → Total de fallecidos
- `Total Affected` → Total de personas afectadas

---

## Proceso de análisis

### 1. Data Cleaning
- Eliminación de 28 columnas innecesarias
- Normalización de nombres de columnas en minúsculas y con guiones bajos
- Tratamiento de valores nulos (fillna con 0, "Unknown" o mediana)
- Eliminación de 55 filas duplicadas
- Corrección de tipos de datos (float → int)

### 2. Análisis Exploratorio (EDA)
- Tendencias temporales de desastres por continente
- Evolución de temperaturas por continente (1950-2021)
- Cruce entre desastres y temperatura global

### 3. Visualizaciones
- Evolución de desastres naturales (1900-2021)
- Total de desastres por continente
- Evolución de temperatura media por continente (1950-2021)
- Cruce desastres vs temperatura global (1950-2021)

---

## Resultados e Insights
-  H1 Confirmada — los desastres aumentaron un 1.500% entre 1900 y 2021
-  H2 Parcialmente confirmada — ambas variables suben juntas desde 1980
-  H3 Confirmada — Asia y América concentran más del 60% de los desastres globales

---

## Obstáculos
- Límite de la API Open-Meteo — esperas de varias horas para descargar datos
- Solo conseguimos 27 de las 45 ciudades planificadas

---

## Próximos pasos
- Completar descarga de las 18 ciudades pendientes
- Ampliar dataset con datos posteriores a 2021
- Muertes por continente y correlación estadística temperatura vs desastres
 

---
 ## Links
 - Presentación Canva: https://canva.link/9hcgyqciv1qkk91