import pandas as pd
import numpy as np


def contar_valores_sd(df):
    """Función para contar la cantidad de valores 'SD' por cada columna y calcular su porcentaje,
    excluyendo las columnas con cero valores 'SD'."""
    resultados = []
    
    for columna in df.columns:
        if columna not in ['columna', 'sd', 'SD', 'total']:  # Excluir las filas especiales
            conteo_SD = (df[columna] == 'SD').sum()
            porcentaje_SD = (conteo_SD / len(df)) * 100  # Calcular el porcentaje
            
            # Agregar los resultados solo si hay al menos un valor 'SD' en la columna
            if conteo_SD > 0:
                resultados.append({'Columna': columna, 'Cantidad de SD': conteo_SD, 'Porcentaje de SD': porcentaje_SD})

    # Convertir la lista de resultados en un DataFrame
    resultado = pd.DataFrame(resultados)

    return resultado


def data_cleaned(df, drop_duplicates=False, drop_na=False, fill_na=None, convert_to_datetime=None, 
                 uppercase_columns=None,lowercase_columns=None, titlecase_columns=None, 
                 strip_spaces=True, rename_columns=None, drop_columns=None,
                 categorize_columns=None, replace_values=None, convert_date_columns=None, 
                  convert_to_int_columns=None, convert_to_float=None):


    df_cleaned = df.copy()

    # 1. Eliminar duplicados
    if drop_duplicates:
        df_cleaned.drop_duplicates(inplace=True)
        

    # 2. Eliminar filas con valores nulos
    if drop_na:
        df_cleaned.dropna(inplace=True)
        

    # 3. Rellenar valores nulos
    if fill_na:
        df_cleaned.fillna(fill_na, inplace=True)
    

    # 4.Convertir columnas a mayúsculas
    if uppercase_columns:
        for column in uppercase_columns:
            df_cleaned[column] = df_cleaned[column].str.upper()
            

    # 5.Convertir columnas a minúsculas
    if lowercase_columns:
        for column in lowercase_columns:
            df_cleaned[column] = df_cleaned[column].str.lower()


    # 6.Convertir columnas a formato de título
    if titlecase_columns:
        for column in titlecase_columns:
            df_cleaned[column] = df_cleaned[column].str.title()


    # 7. Convertir columnas a tipo datetime
    if convert_to_datetime:
        for column in convert_to_datetime:
            df_cleaned[column] = pd.to_datetime(df_cleaned[column], errors='coerce')
                      
            
    # 8.Tratar columnas con espacios
    if strip_spaces:
        df_cleaned = df_cleaned.apply(lambda x: x.strip() if isinstance(x, str) else x)
       #df_cleaned = df_cleaned.applymap(lambda x: x.strip() if isinstance(x, str) else x)   

    # 9.Renombrar columnas
    if rename_columns:
        df_cleaned.rename(columns=rename_columns, inplace=True)
        
    
    # 10.Eliminar columnas
    if drop_columns:
        df_cleaned.drop(columns=drop_columns, inplace=True)
        
        
    # 11. Categorizar columnas
    if categorize_columns:
        for column in categorize_columns:
            if column in df_cleaned.columns:
                df_cleaned[column] = df_cleaned[column].astype('category')
            else:
                print(f"La columna '{column}' no existe en el DataFrame.")
                
                 
    # 12. Convertir columnas de fecha con formato específico
    if convert_date_columns:
        for column, date_format in convert_date_columns.items():
            df_cleaned[column] = pd.to_datetime(df_cleaned[column], format=date_format, errors='coerce')

    
    # 13. Convertir columnas a tipo de dato entero
    if convert_to_int_columns:
        for column in convert_to_int_columns:
            df_cleaned[column] = pd.to_numeric(df_cleaned[column], errors='coerce').astype('Int64')
    
    
    # 14. Convertir columnas a tipo float
    if convert_to_float:
        for column in convert_to_float:
            df_cleaned[column] = df_cleaned[column].astype(float)
        

    # 15. Reemplazar valores en columnas
    if replace_values:
        for column, replacements in replace_values.items():
            #df_cleaned[column].replace(replacements, inplace=True)
            #df_cleaned.replace({column: replacements}, inplace=True)
            df_cleaned[column] = df_cleaned[column].replace(replacements)

    return df_cleaned