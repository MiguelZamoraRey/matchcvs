import pandas as pd

# Rutas de archivos
big_file = "big.csv" # El nombre del csv que exportais del excel grande
little_file = "little.csv" # El nombre del csv que exportais del excel chiquito 
result_file = "result.csv" # Donde se cargaran los resultados comunes

# Nombre de la columna común
id_column = "Identificador" # campo por el que coinciden, es decir, que esta en el segundo y el primero y por el que quereis filtrar

# Cargar los CSV
big_df = pd.read_csv(big_file, dtype=str)  # dtype=str para no perder ceros a la izquierda
little_df = pd.read_csv(little_file, dtype=str)

# Extraer identificadores del pequeño
ids = set(little_df[id_column].dropna().unique())

# Filtrar el grande
filtered_df = big_df[big_df[id_column].isin(ids)]

# Guardar el resultado
filtered_df.to_csv(result_file, index=False)

print(f"Se han encontrado {len(filtered_df)} registros coincidentes.")
print(f"Archivo guardado como {result_file}")