lista_de_listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

maximos = [max(lista) for lista in lista_de_listas]

print(maximos)

import pdb

lista_de_listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

pdb.set_trace()

maximos = [max(lista) for lista in lista_de_listas]

print(maximos)

# Función filter

def es_primo(n):
    """Función que determina si un número es primo"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros = [3, 4, 8, 5, 5, 22, 13]

primos = list(filter(es_primo, numeros))

print(primos)