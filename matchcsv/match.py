import pandas as pd
import chardet

# --- Función para detectar la codificación del archivo ---
def detectar_encoding(ruta):
    with open(ruta, 'rb') as f:
        resultado = chardet.detect(f.read(100000))
    return resultado['encoding']

# --- Pedir datos al usuario ---
big_file = input("Nombre del CSV grande (ej: big.csv): ").strip()
little_file = input("Nombre del CSV pequeño (ej: little.csv): ").strip()

try:
    big_col_index = int(input("Número de columna del CSV grande para comparar (1 = primera columna): ")) - 1
    little_col_index = int(input("Número de columna del CSV pequeño para comparar (1 = primera columna): ")) - 1
except ValueError:
    print("Error: Debes escribir un número de columna válido.")
    exit()

result_file = input("Nombre del CSV de salida (Enter = result.csv): ").strip()
if not result_file:
    result_file = "result.csv"

# --- Detectar codificación ---
big_encoding = detectar_encoding(big_file)
little_encoding = detectar_encoding(little_file)

# --- Cargar CSV sin encabezado fijo ---
big_df = pd.read_csv(big_file, dtype=str, header=None, encoding=big_encoding)
little_df = pd.read_csv(little_file, dtype=str, header=None, encoding=little_encoding)

# --- Extraer identificadores ---
ids = set(little_df.iloc[:, little_col_index].dropna().unique())

# --- Filtrar ---
filtered_df = big_df[big_df.iloc[:, big_col_index].isin(ids)]

# --- Guardar resultado ---
filtered_df.to_csv(result_file, index=False, header=False, encoding="utf-8-sig")

print(f"\n✅ Se han encontrado {len(filtered_df)} registros coincidentes.")
print(f"📄 Archivo guardado como: {result_file}")
