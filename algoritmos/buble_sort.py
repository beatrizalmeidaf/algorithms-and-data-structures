array = [4, 2, 7, 1, 3]

n = len(array)

# loop externo faz isso varias vezes
for j in range(n):
    for i in range(n - j - 1): # evita comparacoes desnecessarias com o que já está ordenado
        if array[i] > array[i+1]:
            aux = array[i]
            array[i] = array[i+1]
            array[i+1] = aux

print(array)