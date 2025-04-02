def suma_cuadrados_iterativa(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i**2
    return suma

def suma_cuadrados_recursiva(n):
    if n == 1:  
        return 1
    else:
        return n**2 + suma_cuadrados_recursiva(n - 1)  

def suma_cuadrados_formula(n):
    return n * (n + 1) * (2 * n + 1) // 6

x = 100
assert suma_cuadrados_iterativa(x) == suma_cuadrados_recursiva(x) == suma_cuadrados_formula(x), "¡Las funciones no coinciden!"

print(" Todas las funciones dan el mismo resultado.")

import timeit

n = 10

print("n = ",n)

print("tiempo iterativa: ", timeit.timeit(lambda: suma_cuadrados_iterativa(n)), "segundos")
print("tiempo recursivo: ", timeit.timeit(lambda: suma_cuadrados_recursiva(n)), "segundos")
print("tiempo formula: ", timeit.timeit(lambda: suma_cuadrados_formula(n)), "segundos")