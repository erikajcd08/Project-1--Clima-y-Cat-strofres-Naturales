# Project-1--Clima-y-Cat-strofres-Naturales
# Proyecto 1: Clima y Catástofres Naturales

## Introducciñon del proyecto

El objetivo de este proyecto es analizar los datos entre el cambio climático y los desastres naturales a nivel global, comparando las tendencias por continente y región entre los años 1900 y 2021.

---

## Dataset

- **Fuente 1:** EM-DAT- All Natural Disasters 1900- 2021 de Kaggle:
        -- 16.701 registros de desastres naturales a nivel global
        -- Link del dataset: https://www.kaggle.com/datasets/brsdincer/all-natural-disasters-19002021-eosdis
- **Fuente 2:** En progreso
        -- API gratuita de datos climáticos históricos

---

# Hipótesis
- 1. Los desastres naturales han aumentado progresivamente por continente¿?
- 2. El número de desastres ha crecido en paralelo al aumento de las temperaturas
- 3. Algunas regiones son más vulnerables a dichas catástofres que otras.

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

---

## Resultados e Insights
*(En progreso)*

---


## Resultados / Insights
*(Se completará al finalizar el análisis)*
- Conclusiones sobre la evolución de desastres por continente
- Relación entre temperaturas y frecuencia de desastres
- Regiones más vulnerables identificadas


---

## Próximos pasos
*(Qué haría si tuviera más tiempo o datos)*
- Incorporar datos de temperatura de la API Open-Meteo 
  para correlacionar con los desastres
- Analizar el impacto económico por región con más detalle
- Estudiar la relación entre el PIB de cada país y 
  su capacidad de respuesta ante desastres
- Ampliar el dataset con datos posteriores a 2021
- Analizar el impacto del cambio climático en tipos 
  específicos de desastres (inundaciones, sequías...)
 

---
 ## Links
 - Trello:
 - Presentación Canva: