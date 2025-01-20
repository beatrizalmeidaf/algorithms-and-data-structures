import numpy as np

def reverseArray(array):
    array = np.array(array)
    reversed_array = np.empty_like(array) # criar array vazio

    for i in range(len(array)):
        reversed_array[i] = array[len(array) -1 - i]

    return reversed_array

if __name__ == '__main__':
    array = list(map(int, input("Informe os valores do array: ").split()))
    array_reverso = reverseArray(array)
    print(array_reverso)

