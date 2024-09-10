# Función que valida y combina entradas de usuario
def procesar_entrada(nombre, edad):
    nombre_valido = nombre if nombre is not None else "Anónimo"
    edad_valida = edad if edad is not None else "Edad no proporcionada"
    
    return f"Nombre: {nombre_valido}, Edad: {edad_valida}"

# Ejemplos de entradas de usuario
print(procesar_entrada("Carlos", None))  # Nombre válido, edad no proporcionada
print(procesar_entrada(None, 25))  # Nombre no proporcionado, edad válida
print(procesar_entrada(None, None))  # Ningún valor proporcionado
