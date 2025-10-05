import itertools

def eh_quadrado_magico(v):
    # v é uma lista com 9 números, representando o quadrado linha por linha
    return (
        sum(v[0:3]) == sum(v[3:6]) == sum(v[6:9]) ==  # Linhas
        sum(v[0::3]) == sum(v[1::3]) == sum(v[2::3]) ==  # Colunas
        v[0] + v[4] + v[8] == v[2] + v[4] + v[6]  # Diagonais
    )

def quadrados_magicos():
    numeros = [1,2,3,4,5,6,7,8,9]
    for p in itertools.permutations(numeros):
        if eh_quadrado_magico(p):
            print(f"{p[0]} {p[1]} {p[2]}")
            print(f"{p[3]} {p[4]} {p[5]}")
            print(f"{p[6]} {p[7]} {p[8]}")
            print("-" * 10)

quadrados_magicos()
