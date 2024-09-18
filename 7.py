def terceiro_maior(arr):
    # Converte o vetor em um conjunto para eliminar duplicatas
    conjunto_unico = set(arr)

    # Verifica se há pelo menos três elementos únicos
    if len(conjunto_unico) < 3:
        raise ValueError("O vetor deve conter pelo menos três números diferentes.")

    # Ordena os elementos únicos em ordem decrescente
    lista_ordenada = sorted(conjunto_unico, reverse=True)
    return lista_ordenado[2]  # Retorna o terceiro maior


# Testando a função
if __name__ == "__main__":
    vetor = [64, 25, 12, 22, 11, 25, 12]

    terceiro_maior_num = terceiro_maior(vetor)

    print("O terceiro maior número é:", terceiro_maior_num)
