def fibonacci(n):
    fib_secuencia = [0, 1]

    while len(fib_secuencia) < n:
        fib_secuencia.append(fib_secuencia[-1] + fib_secuencia[-2])

    return fib_secuencia[:n]

# Solicitar al usuario el número de términos deseado
n = int(input("Ingrese la cantidad de términos de la serie de Fibonacci que desea calcular: "))

# Validar entrada
if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    result = fibonacci(n)
    print(f"Serie de Fibonacci con {n} términos: {result}")
