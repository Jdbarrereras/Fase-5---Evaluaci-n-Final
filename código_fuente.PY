# ============================================
# Nombre: Jonathan Barrera
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final
# Problema 1 - Clasificación de compromiso
# Código fuente: Autoría propia
# ============================================

# Matriz de datos
sesiones = [
    ["C001", 250, 10],
    ["C002", 40, 2],
    ["C003", 120, 5],
    ["C004", 300, 15],
    ["C005", 50, 7]
]

# Función para clasificar el compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Mostrar resultados
print("INFORME DE COMPROMISO DE CLIENTES\n")

for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente)
    print("Duración:", duracion, "segundos")
    print("Clics:", clics)
    print("Clasificación:", clasificacion)
    print("-----------------------------")