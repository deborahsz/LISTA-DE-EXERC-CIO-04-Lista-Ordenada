def remover_duplicatas(arr):
    resultado = []  # Cria uma lista vazia para armazenar os elementos únicos
    for num in arr:
        if num not in resultado:  # Verifica se o número já está na lista de resultados
            resultado.append(num)  # Se não estiver, adiciona à lista
    return resultado


# Testando a função
if __name__ == "__main__":
    vetor = [64, 25, 12, 22, 11, 12, 25]

    vetor_sem_duplicatas = remover_duplicatas(vetor)

    print("Vetor original:", vetor)
    print("Vetor sem duplicatas:", vetor_sem_duplicatas)
