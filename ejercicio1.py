# Función que suma todos los números enteros hasta 'n' usando memoización
def suma_hasta_n(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    memo[n] = n + suma_hasta_n(n - 1, memo)
    return memo[n]

# Calcular la suma de números hasta 1000
resultado = suma_hasta_n(1000)
print("La suma de números hasta 1000 es:", resultado)
