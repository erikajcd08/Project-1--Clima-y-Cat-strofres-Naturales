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
- Tipos de desastres más frecuentes y mortales
- Comparación de impacto humano por región-

### 3. Visualizaciones
*(En progreso)*
- Evolución de desastres naturales (1900-2021)
- Total de desastres por continente
- Evolución de temperatura media por continente *(en progreso)*

---

## Resultados e Insights
*(En progreso)*
- Los desastres naturales aumentaron drásticamente a partir de 1960
- Pico máximo de desastres registrado entre 2000 y 2005
- Asia concentra el mayor número de desastres (~6.000)
- América ocupa el segundo lugar (~4.000)
- Las temperaturas en Europa y Asia muestran una tendencia al alza

---


## Resultados / Insights
*(Se completará al finalizar el análisis)*
- Los desastres naturales aumentaron drásticamente a partir de 1960
- Pico máximo de desastres registrado entre 2000 y 2005
- Asia concentra el mayor número de desastres (~6.000)
- América ocupa el segundo lugar (~4.000)
- Las temperaturas en Europa y Asia muestran una tendencia al alza


---

## Próximos pasos
*(Qué haría si tuviera más tiempo o datos)*
- Incorporar datos de temperatura de la API Open-Meteo para correlacionar con los desastres de América, África y Oceanía
- Analizar el impacto económico por región con más detalle
- Estudiar la relación entre el PIB de cada país y su capacidad de respuesta ante desastres
- Ampliar el dataset con datos posteriores a 2021
- Analizar el impacto del cambio climático en tipos específicos de desastres (inundaciones, sequías...)
- Análisis por tipo de desastre más frecuente
 

---
 ## Links
 - Trello:
 - Presentación Canva: