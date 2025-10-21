import math
import pandas as pd

# Función para calcular la entropía
def entropia(p, n):
    if p == 0 or n == 0:
        return 0
    total = p + n
    p_ratio = p / total
    n_ratio = n / total
    return - (p_ratio * math.log2(p_ratio) + n_ratio * math.log2(n_ratio))

# Función para calcular la ganancia de información
def ganancia_info(total_p, total_n, divisiones):
    entropia_total = entropia(total_p, total_n)
    total = total_p + total_n
    entropia_ponderada = sum(
        ((p + n) / total) * entropia(p, n) for p, n in divisiones
    )
    ganancia = entropia_total - entropia_ponderada
    return entropia_total, entropia_ponderada, ganancia

# 1. Cargar los datos
data = pd.DataFrame({
    "Edad": [24, 38, 29, 45, 52, 33, 41, 27, 36, 31],
    "UsoGB": [2.5, 6.0, 3.0, 8.0, 7.5, 4.0, 5.5, 2.0, 6.5, 3.5],
    "LineaFija": ["No", "Sí", "No", "Sí", "Sí", "No", "Sí", "No", "Sí", "No"],
    "Acepta": ["No", "Sí", "No", "Sí", "Sí", "No", "Sí", "No", "Sí", "No"]
})

# 2. Entropía del conjunto original
p_total = (data["Acepta"] == "Sí").sum()
n_total = (data["Acepta"] == "No").sum()

print("=== 1. ENTROPÍA DEL CONJUNTO ORIGINAL ===")
print(f"Positivos (Sí): {p_total}, Negativos (No): {n_total}")
print(f"Entropía total: {entropia(p_total, n_total):.4f}")

# 3. Evaluar atributos
print("\n=== 2. GANANCIA DE INFORMACIÓN POR ATRIBUTO ===")

# Edad agrupada
bins_edad = [0, 30, 50, 100]
labels_edad = ["Joven", "Adulto", "Mayor"]
data["EdadGrupo"] = pd.cut(data["Edad"], bins=bins_edad, labels=labels_edad)

tabla_edad = data.groupby("EdadGrupo", observed=False)["Acepta"].value_counts().unstack().fillna(0)
divisiones_edad = [(row.get("Sí", 0), row.get("No", 0)) for _, row in tabla_edad.iterrows()]
_, _, ganancia_edad = ganancia_info(p_total, n_total, divisiones_edad)
print("-- Edad agrupada --")
print(tabla_edad)
print(f"Edad → Ganancia: {ganancia_edad:.4f}")

# Línea fija
tabla_linea = data.groupby("LineaFija", observed=False)["Acepta"].value_counts().unstack().fillna(0)
divisiones_linea = [(row.get("Sí", 0), row.get("No", 0)) for _, row in tabla_linea.iterrows()]
_, _, ganancia_linea = ganancia_info(p_total, n_total, divisiones_linea)
print("\n-- Línea fija --")
print(tabla_linea)
print(f"Línea fija → Ganancia: {ganancia_linea:.4f}")

# Uso de datos agrupado
bins_uso = [0, 3, 6, 100]
labels_uso = ["Bajo", "Medio", "Alto"]
data["UsoGrupo"] = pd.cut(data["UsoGB"], bins=bins_uso, labels=labels_uso)

tabla_uso = data.groupby("UsoGrupo", observed=False)["Acepta"].value_counts().unstack().fillna(0)
divisiones_uso = [(row.get("Sí", 0), row.get("No", 0)) for _, row in tabla_uso.iterrows()]
_, _, ganancia_uso = ganancia_info(p_total, n_total, divisiones_uso)
print("\n-- Uso de datos agrupado --")
print(tabla_uso)
print(f"Uso de datos → Ganancia: {ganancia_uso:.4f}")
