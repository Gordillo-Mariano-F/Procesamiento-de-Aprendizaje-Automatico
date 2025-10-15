import pandas as pd

# Datos de ejemplo
data = {
    'Usuario': ['user1', 'user2', 'user3', 'user4', 'user5'],
    'Accion': ['Combate', 'Exploración', 'Interaccion Social', 'Combate', 'Exploración'],
    'Duración': [120, 300, 180, 90, 240]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Función para clasificar el resultado de la acción
def clasificar_accion(fila):
    accion = fila['Accion']
    duracion = fila['Duración']
    
    if accion == 'Interaccion Social' and duracion >= 180:
        return 'Mensaje Enviado'
    elif accion == 'Exploración' and duracion >= 300:
        return 'Descubrimiento'
    elif accion == 'Combate' and duracion >= 120:
        return 'Victoria'
    else:
        return 'Derrota'

# Aplicar la clasificación al DataFrame
df['Resultado'] = df.apply(clasificar_accion, axis=1)

print(df.to_string(index=False))
