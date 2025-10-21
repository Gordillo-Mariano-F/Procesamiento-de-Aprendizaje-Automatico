import math

# Datos de entrada
datos = [ 
    {"edad": 22, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True}, 
    {"edad": 24, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": True}, 
    {"edad": 21, "departamento": "RRHH", "nivel_educativo": "terciario", "en_formacion": True}, 
    {"edad": 35, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": False}, 
    {"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría", "en_formacion": False}, 
    {"edad": 29, "departamento": "RRHH", "nivel_educativo": "universitario", "en_formacion": False}, 
    {"edad": 23, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True}, 
    {"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False}
]

# Separar positivos y negativos
positivos = [d for d in datos if d["en_formacion"]]
negativos = [d for d in datos if not d["en_formacion"]]

# Identificar valores únicos en positivos
departamentos_positivos = set(d["departamento"] for d in positivos)
departamentos_negativos = set(d["departamento"] for d in negativos)
departamentos_exclusivos = departamentos_positivos - departamentos_negativos

niveles_positivos = set(d["nivel_educativo"] for d in positivos)
niveles_negativos = set(d["nivel_educativo"] for d in negativos)
niveles_exclusivos = niveles_positivos - niveles_negativos

edades_positivos = set(d["edad"] for d in positivos)
edades_negativos = set(d["edad"] for d in negativos)
edades_exclusivas = edades_positivos - edades_negativos

# Mostrar regla inducida
print("Regla inducida para identificar empleados en formación:")
print(f"- Departamentos exclusivos en positivos: {departamentos_exclusivos if departamentos_exclusivos else 'Ninguno'}")
print(f"- Niveles educativos exclusivos en positivos: {niveles_exclusivos}")
print(f"- Edades exclusivas en positivos: {sorted(edades_exclusivas)}")
print()

# Función para calcular FOIL Gain
def calcular_foil_gain(positivos, negativos, condicion, descripcion):
    positivos_despues = [d for d in positivos if condicion(d)]
    negativos_despues = [d for d in negativos if condicion(d)]
    p, n = len(positivos_despues), len(negativos_despues)
    P, N = len(positivos), len(negativos)
    
    frac1 = p / (p + n) if (p + n) > 0 else 0
    frac2 = P / (P + N)
    
    gain = p * (math.log2(frac1) - math.log2(frac2)) if frac1 > 0 else 0

    print(f"Evaluando condición: {descripcion}")
    print(f"P = {P}, N = {N}, p = {p}, n = {n}")
    print(f"p / (p + n) = {frac1:.3f}")
    print(f"P / (P + N) = {frac2:.3f}")
    print(f"FOIL Gain = {gain:.3f}")
    print("-" * 50)

# Evaluar FOIL Gain para condiciones relevantes
calcular_foil_gain(positivos, negativos, lambda d: d["nivel_educativo"] == "terciario", "nivel_educativo == 'terciario'")
calcular_foil_gain(positivos, negativos, lambda d: d["departamento"] == "IT", "departamento == 'IT'")
calcular_foil_gain(positivos, negativos, lambda d: d["edad"] < 30, "edad < 30")
