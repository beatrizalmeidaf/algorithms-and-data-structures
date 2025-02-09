array = [4, 2, 7, 1, 3]

n = len(array)
for j in range(n - 1):
    min_index = j
    for i in range(j + 1, n): # percorre os elementos à frente
        if array[i] < array[min_index]:
            min_index = i

    array[j], array[min_index] = array[min_index], array[j]

print(array)