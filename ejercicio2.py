from decimal import Decimal, getcontext

# Establecer precisión alta
getcontext().prec = 30

# Cálculo preciso de una raíz cuadrada usando Decimal
numero = Decimal('2')
raiz_cuadrada = numero.sqrt()

# Mostramos el resultado con precisión
print(f"Raíz cuadrada precisa de 2: {raiz_cuadrada}")
