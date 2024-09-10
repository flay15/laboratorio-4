import re

# Cadena con múltiples patrones y texto
cadena = "Los precios son $30, $45.50 y $99.99. ¿Cuál es tu preferencia?"

# Expresión regular para encontrar precios en formato de dólares
patron = r'\$\d+\.\d{2}|\$\d+'

# Sustitución para convertir precios en formato de euros (€)
cadena_euros = re.sub(patron, lambda x: '€' + x.group()[1:], cadena)

print("Cadena con precios en euros:", cadena_euros)
