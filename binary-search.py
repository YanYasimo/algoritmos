import time
def pesquisa_binaria(lista, elemento):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2  # Calcula o índice do meio da lista

        if lista[meio] == elemento:
            return meio  # O elemento foi encontrado, retornamos o índice
        elif lista[meio] < elemento:
            esquerda = meio + 1  # O elemento está à direita do meio
        else:
            direita = meio - 1  # O elemento está à esquerda do meio

    return -1  # Se o elemento não foi encontrado, retornamos -1

# Exemplo de uso com uma lista grande de até 1 milhão de números:

minha_lista = list(range(1, 100000001))  # Gera uma lista ordenada de 1 a 1.000.000
elemento_desejado = 9999999

# Medir o tempo de execução
inicio = time.time()
resultado = pesquisa_binaria(minha_lista, elemento_desejado)
fim = time.time()

if resultado != -1:
    print(f'O elemento {elemento_desejado} foi encontrado no índice {resultado}.')
else:
    print(f'O elemento {elemento_desejado} não foi encontrado na lista.')

tempo_total_millissegundos = (fim - inicio) * 1000
print(f"Tempo levado para a pesquisa binária: {tempo_total_millissegundos:.2f} milissegundos")