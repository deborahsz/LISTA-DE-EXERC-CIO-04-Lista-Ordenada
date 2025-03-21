def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Testando a função
if __name__ == "__main__":
    vetor = [64, 25, 12, 22, 11]
    print("Vetor original:", vetor)
    vetor_ordenado = selection_sort(vetor)
    print("Vetor ordenado:", vetor_ordenado)
