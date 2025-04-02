def suma_iterativa(n):
    suma = 0
    for i in range (1, n + 1):
        suma +=i
    return suma

def suma_recursiva(n):
    if n == 0:
        return 0
    return n + suma_recursiva(n -1)

def suma_formula(n):
    return n * (n + 1) // 2

x = 100

assert suma_iterativa(x) == suma_recursiva(x) == suma_formula(x), "¡Las funciones no coinciden!"

print(" Todas las funciones dan el mismo resultado.")

import timeit

n = 1000

print("n = ",n)

print("tiempo iterativa: ", timeit.timeit(lambda: suma_iterativa(n)), "segundos")
print("tiempo recursivo: ", timeit.timeit(lambda: suma_recursiva(n)), "segundos")
print("tiempo formula: ", timeit.timeit(lambda: suma_formula(n)), "segundos")