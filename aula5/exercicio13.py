def desenha_moldura(linhas=1, colunas=1):
    # Garante que os valores fiquem dentro da faixa [1, 20]
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))
    
    # Cálculo da parte horizontal (entre os cantos +)
    horizontal = '-' * colunas
    
    # Linha superior
    print('+' + horizontal + '+')
    
    # Linhas do meio
    for _ in range(linhas):
        print('|' + ' ' * colunas + '|')
    
    # Linha inferior
    print('+' + horizontal + '+')

# Exemplos de uso:
desenha_moldura(3, 8)
print()
desenha_moldura(25, -5)
