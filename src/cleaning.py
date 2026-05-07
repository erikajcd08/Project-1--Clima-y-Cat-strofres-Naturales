import pandas as pd

def load_data(filepath):
    """Carga el dataset desde la ruta especificada"""
    df = pd.read_csv(filepath)
    return df

def drop_unnecessary_columns(df):
    """Elimina columnas que no son necesarias para el análisis"""
    cols_to_drop = [
        'Seq', 'Glide', 'Disaster Subsubtype', 'Event Name',
        'Origin', 'Associated Dis', 'Associated Dis2',
        'OFDA Response', 'Appeal', 'Declaration',
        'Aid Contribution', 'Dis Mag Value', 'Dis Mag Scale',
        'Latitude', 'Longitude', 'Local Time', 'River Basin',
        'Start Month', 'Start Day', 'End Month', 'End Day',
        'No Injured', 'No Homeless', "Insured Damages ('000 US$)",
        'Adm Level', 'Admin1 Code', 'Admin2 Code', 'Geo Locations',
        "Total Damages ('000 US$)"
    ]
    return df.drop(columns=cols_to_drop)

def normalize_column_names(df):
    """Normaliza los nombres de columnas a minúsculas y con guiones bajos"""
    df.columns = (df.columns
                  .str.lower()
                  .str.replace(' ', '_')
                  .str.replace("'", '')
                  .str.replace('(', '')
                  .str.replace(')', '')
                  .str.replace('$', ''))
    return df

def handle_nulls(df):
    """Trata los valores nulos de cada columna"""
    # Columnas de texto
    df["disaster_subtype"] = df["disaster_subtype"].fillna("Unknown")
    df["location"] = df["location"].fillna("Unknown")
    # Columnas numéricas
    df["total_deaths"] = df["total_deaths"].fillna(0)
    df["no_affected"] = df["no_affected"].fillna(0)
    df["total_affected"] = df["total_affected"].fillna(0)
    # CPI con mediana
    df["cpi"] = df["cpi"].fillna(df["cpi"].median())
    return df

def fix_dtypes(df):
    """Corrige los tipos de datos de columnas numéricas"""
    df["total_deaths"] = df["total_deaths"].astype(int)
    df["no_affected"] = df["no_affected"].astype(int)
    df["total_affected"] = df["total_affected"].astype(int)
    return df

def remove_duplicates(df):
    """Elimina filas completamente duplicadas"""
    return df.drop_duplicates()

def clean_disasters(filepath):
    """Función principal que ejecuta todo el proceso de limpieza"""
    df = load_data(filepath)
    df = drop_unnecessary_columns(df)
    df = normalize_column_names(df)
    df = handle_nulls(df)
    df = fix_dtypes(df)
    df = remove_duplicates(df)
    print(f"Dataset limpio: {df.shape[0]} filas, {df.shape[1]} columnas ok")
    return df