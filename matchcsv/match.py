import pandas as pd

# Rutas de archivos
big_file = "big.csv" # El nombre del csv que exportais del excel grande
little_file = "little.csv" # El nombre del csv que exportais del excel chiquito 
result_file = "result.csv" # Donde se cargaran los resultados comunes

# Índices de columna (0 = primera columna)
big_col_index = 2   # Columna 3 en big.csv
little_col_index = 4  # Columna 5 en little.csv

# Cargar CSV sin encabezados fijos (para indexar por número)
big_df = pd.read_csv(big_file, dtype=str)
little_df = pd.read_csv(little_file, dtype=str)

# Extraer la columna deseada del pequeño
ids = set(little_df.iloc[:, little_col_index].dropna().unique())

# Filtrar el grande según su columna correspondiente
filtered_df = big_df[big_df.iloc[:, big_col_index].isin(ids)]

# Guardar resultado
filtered_df.to_csv(result_file, index=False)

print(f"Se han encontrado {len(filtered_df)} registros coincidentes.")
print(f"Archivo guardado como {result_file}")
