def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    # Move o pivô para o final
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[right] = arr[right], arr[store_index]
    return store_index

def median_of_medians(arr, left, right, r):
    """
    Se o intervalo tiver menos de r elementos, ordena e retorna a mediana.
    Caso contrário, divide o intervalo em grupos de tamanho r, calcula a mediana
    de cada grupo e recursivamente retorna a mediana dessas medianas.
    """
    if right - left < r:
        return sorted(arr[left:right+1])[(right - left) // 2]
    
    medians = []
    for i in range(left, right + 1, r):
        subgroup = sorted(arr[i: min(i + r, right + 1)])
        medians.append(subgroup[len(subgroup) // 2])
    
    # Recursivamente, encontra a mediana das medianas
    return select(medians, 0, len(medians) - 1, len(medians) // 2, r)

def select(arr, left, right, k, r):
    """
    Retorna o k-ésimo menor elemento (k com base 0) no subvetor arr[left:right+1].
    """
    if left == right:
        return arr[left]

    pivot = median_of_medians(arr, left, right, r)
    # Busca a posição do pivô; usamos o primeiro encontrado no subintervalo
    pivot_index = arr.index(pivot, left, right+1)
    pivot_index = partition(arr, left, right, pivot_index)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return select(arr, left, pivot_index - 1, k, r)
    else:
        return select(arr, pivot_index + 1, right, k, r)

def select_bfprt(arr, k, r=5):
    """
    Função wrapper que recebe:
      - arr: vetor de elementos;
      - k: posição desejada (0-indexado, ou seja, k = 0 retorna o menor elemento);
      - r: tamanho do grupo para o cálculo da mediana de medianas.
    Retorna o k-ésimo menor elemento.
    """
    return select(arr, 0, len(arr) - 1, k, r)

if __name__ == "__main__":
    # Teste rápido:
    vetor = [12, 3, 5, 7, 19, 26, 4, 2, 9, 23, 90, 7, 3, 2, 65]
    k = 3  # Para buscar o 3º menor elemento (considerando indexação 0: [menor, 2º, 3º, ...])
    resultado = select_bfprt(vetor, k)
    print("K-th smallest element é:", resultado)
