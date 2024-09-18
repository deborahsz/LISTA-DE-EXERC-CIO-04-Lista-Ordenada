def encontrar_maximo(arr):
    maximo = arr[0]  # Assume que o primeiro elemento é o máximo
    for num in arr:
        if num > maximo:
            maximo = num
    return maximo


def encontrar_minimo(arr):
    minimo = arr[0]  # Assume que o primeiro elemento é o mínimo
    for num in arr:
        if num < minimo:
            minimo = num
    return minimo


# Testando as funções
if __name__ == "__main__":
    vetor = [64, 25, 12, 22, 11]

    maximo = encontrar_maximo(vetor)
    minimo = encontrar_minimo(vetor)

    print("Elemento máximo:", maximo)
    print("Elemento mínimo:", minimo)
