def segundo_menor(arr):
    # Converte o vetor em um conjunto para eliminar duplicatas
    conjunto_unico = set(arr)

    # Verifica se há pelo menos dois elementos únicos
    if len(conjunto_unico) < 2:
        raise ValueError("O vetor deve conter pelo menos dois números diferentes.")

    # Ordena os elementos únicos e pega o segundo menor
    lista_ordenada = sorted(conjunto_unico)
    return lista_ordenada[1]


# Testando a função
if __name__ == "__main__":
    vetor = [64, 25, 12, 22, 11, 12, 25]

    segundo_menor_num = segundo_menor(vetor)

    print("O segundo menor número é:", segundo_menor_num)
