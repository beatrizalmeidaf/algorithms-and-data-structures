array = [4, 2, 7, 1, 3]


for i in range(1, len(array)):
    temp = array[i] # valor atual
    j = i - 1 # compara com o anterior
    
    while j>=0 and array[j] > temp:
        array[j + 1] = array[j] # move para a direita
        j -= 1 

    array[j + 1] = temp

print("Array ordenado:", array)