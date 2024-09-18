def sort_array(arr, ordem='crescente'):
    if ordem == 'crescente':
        arr.sort()  # Ordena em ordem crescente
    elif ordem == 'decrescente':
        arr.sort(reverse=True)  # Ordena em ordem decrescente
    else:
        raise ValueError("O parâmetro 'ordem' deve ser 'crescente' ou 'decrescente'.")

    return arr


# Testando a função
if __name__ == "__main__":
    vetor = [64, 25, 12, 22, 11]

    # Ordenando em ordem crescente
    print("Vetor original:", vetor)
    vetor_crescente = sort_array(vetor.copy(), 'crescente')
    print("Vetor ordenado em ordem crescente:", vetor_crescente)

    # Ordenando em ordem decrescente
    vetor_decrescente = sort_array(vetor.copy(), 'decrescente')
    print("Vetor ordenado em ordem decrescente:", vetor_decrescente)
