import gmpy2
import random
import time

"""
PRUEBAS RECOMENDADAS:

# Casos fáciles (rápidos)
5959                # 59 * 101
10403               # 101 * 103

# Casos grandes
10007*10009         # factores cercanos
1000003*1000033     # grande y cercano

# Casos difíciles
1009*13             # factores lejanos

# Primo (no factorizable)
10000019
"""

respuesta = "si"

while respuesta.lower() == "si":
    n = gmpy2.mpz(input("Digite el número: "))

    inicio = time.time()

    p = None
    intentos = 0

    while p is None:
        intentos += 1

        # Paso 1: y aleatorio en [2, n-2]
        y = gmpy2.mpz(random.randint(2, int(n) - 2))

        # Paso 2: a ≡ y² mod n
        a = gmpy2.powmod(y, 2, n)

        # Paso 3: x tal que x² ≡ a mod n
        # Buscamos x recorriendo desde sqrt(a) hasta encontrar uno que cumpla
        x = gmpy2.isqrt(a)
        encontrado = False
        for candidato in range(int(x), int(x) + 1000):
            if gmpy2.powmod(gmpy2.mpz(candidato), 2, n) == a:
                x = gmpy2.mpz(candidato)
                encontrado = True
                break
        if not encontrado:
            continue

        # Asegurar 0 < x <= n-1
        x = x % n
        if x == 0:
            continue

        # Paso 4: Si x ≡ ±y mod n → trivial, reintentar
        if x % n == y % n or x % n == (-y) % n:
            continue

        # De lo contrario: p = mcd(x - y, n)
        candidato_p = gmpy2.gcd((x - y) % n, n)

        if 1 < candidato_p < n:
            p = candidato_p

    q = n // p
    fin = time.time()

    print("\n--- RESULTADO ---")
    print(f"y: {y},  x: {x}")
    print(f"Factores: {p} y {q}")
    print(f"Iteraciones: {intentos}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")

    respuesta = input("\n¿Desea continuar? (si/no): ")