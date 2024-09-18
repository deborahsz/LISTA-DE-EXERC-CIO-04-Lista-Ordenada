def ordenar_decrescente(arr):
    return sorted(arr, reverse=True)  # Ordena o vetor em ordem decrescente


def contar_pares_impares(arr):
    pares = 0
    impares = 0
    for num in arr:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares


# Testando o programa
if __name__ == "__main__":
    vetor = [64, 25, 12, 22, 11, 5, 30]

    vetor_ordenado = ordenar_decrescente(vetor)
    pares, impares = contar_pares_impares(vetor_ordenado)

    print("Vetor ordenado em ordem decrescente:", vetor_ordenado)
    print("Quantidade de números pares:", pares)
    print("Quantidade de números ímpares:", impares)
