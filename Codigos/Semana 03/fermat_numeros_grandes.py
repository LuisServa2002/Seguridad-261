import gmpy2
import time

"""
PRUEBAS RECOMENDADAS:

# Casos fáciles (rápidos)
5959                # 59 * 101
10403               # 101 * 103

# Casos grandes (buenos para Fermat)
10007*10009         # factores cercanos
1000003*1000033     # grande y cercano

# Casos difíciles
1009*13             # factores lejanos
1234577*3           # muy desbalanceado

# Primo (muy lento en Fermat)
10000019
"""

respuesta = "si"

while respuesta.lower() == "si":
    n = gmpy2.mpz(input("Digite el número: "))

    inicio = time.time()

    a = gmpy2.isqrt(n)
    
    if a * a < n:
        a += 1

    iteraciones = 0

    while True:
        iteraciones += 1

        b2 = a*a - n

        if gmpy2.is_square(b2):
            b = gmpy2.isqrt(b2)
            break

        a += 1

    fin = time.time()

    print("\n--- RESULTADO ---")
    print(f"a: {a}, b: {b}")
    print(f"Factores: {a-b} y {a+b}")
    print(f"Iteraciones: {iteraciones}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")

    respuesta = input("\n¿Desea continuar? (si/no): ")


