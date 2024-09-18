def mediana(vetor):
    # Ordena o vetor
    vetor_ordenado = sorted(vetor)
    # Calcula o índice do elemento do meio
    meio = len(vetor_ordenado) // 2
    # Retorna a mediana
    return vetor_ordenado[meio]

# Exemplo de uso
vetor = [3, 1, 4, 1, 5]
resultado = mediana(vetor)
print(f"A mediana é: {resultado}")
