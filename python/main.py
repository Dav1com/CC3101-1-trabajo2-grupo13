# Grupo 13
# Trabajo 2

CHARS = "BEA"

import time, sys
import numpy as np

def generar(arreglo: list, minimo: int, maximo: int, acumulado: str, diferencia: int, vivos_b: int) -> None:
    """ Función para generar todas las combinaciones de letras validas. """
    # Agregar el string a la lista de secuencias válidas
    # Si su largo esta en el rango correcto
    # Y si no quedan jugadores en el equipo B.
    if (minimo <= len(acumulado) and vivos_b == 0): 
        arreglo.append(acumulado)
        return
    
    # Caso base (Cuando el string sobrepasa el torneo mas largo)
    if len(acumulado) == maximo:    
        return
    
    # Poda (Cuando ya no quedan jugadores en el equipo B)
    if vivos_b < 0:
        return
    
    # Generar recursivamente las 3 variaciones de este string.
    # En orden: +'B', +'E', +'A'
    for i in range(3):
        diferencia += i - 1
        if (diferencia >= 0): # Solo lo intenta si es un torneo que sigue las reglas "arregladas"
            vivos_b -= int(i > 0)
            generar(arreglo, minimo, maximo, acumulado + CHARS[i], diferencia, vivos_b) 
            vivos_b += int(i > 0)
        diferencia -= i - 1    

# Tests
#combinaciones_test = []
#generar(combinaciones_test, 10, 10*2 - 1, "", 0, 10)
#assert len(combinaciones_test) == 1037718

def T(k: int, n: int) -> int:
    """ Función para contar todas las combinaciones de letras validas, recursivamente. """
    if n == 0:
        return 1
    elif k == n:
        return T(k, n-1) + T(k-1, n-1)
    else:
        return T(k, n-1) + T(k-1, n-1) + T(k-1, n)

# Tests
#assert T(0, 0) == 1
#assert T(10, 10) == 1037718
#assert T(6, 3) == 264

def T_tabulacion(m: int) -> int:
    """ Función para contar todas las combinaciones de letras validas, iterativamente, usando tabulación. """
    tabla = np.empty([2, m+1], dtype=np.uint64)
    tabla[:,0] = np.ones(2, dtype=np.uint64)
    for k in range(1,m+1):
        for n in range(1, k):
            tabla[1, n] = tabla[0,n-1] + tabla[1,n-1] + tabla[0,n]
        tabla[1, k] = tabla[0,k-1] + tabla[1,k-1]
        tabla[[0, 1]] = tabla[[1, 0]]
    return tabla[0,m]

# Tests
#assert T_tabulacion(0) == T(0,0)
#assert T_tabulacion(1) == T(1,1)
#assert T_tabulacion(10) == T(10,10)


def parteB() -> None:
    m = int(input("Valor 'm': "))    # Número de jugadores por equipo
    a1 = m              # Torneo mas corto
    a2 = (2 * m) - 1    # Torneo mas largo
    combinaciones = []  # Arreglo de combinaciones válidas
    generar(combinaciones, a1, a2, "", 0, a1)
    print(f"Existen {len(combinaciones)} combinaciones válidas")

def tablaInforme() -> None:
    for i in range(25):
        print(i, ":", T_tabulacion(i))

def permormanceTest(mm: int) -> None:
    print(f"m={mm}")

    start = time.perf_counter()
    print(T_tabulacion(mm))
    print(f"Tabulación DP: Tiempo: {1000*(time.perf_counter() - start)}",)

    start = time.perf_counter()
    print(T(mm, mm))
    print(f"Recursión: Tiempo: {1000*(time.perf_counter() - start)}")

    start = time.perf_counter()
    combinaciones = []
    generar(combinaciones, mm, mm*2 - 1, "", 0, mm)
    print(len(combinaciones))
    print(f"Fuerza bruta: Tiempo: {1000*(time.perf_counter() - start)}")

if __name__ == "__main__":
    sys.setrecursionlimit(1000)

    mm = int(100)
    print(f"Existen {T_tabulacion(mm)} partidos posibles.")
