import time

def criar_array():
    array = []
    size = int(input("Qual o tamanho do seu array?\n"))

    print("\n")

    for i in range(size):
        elemento = input("Insira os numeros do array\n")
        array.append(int(elemento))

    return array

def busca_binaria(array):
    numero = int(input("Qual numero deseja buscar?\n"))

    array.sort() # ordernar o array

    inicio, fim = 0, len(array) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if array[meio] == numero:
            print("Número encontrado no array!")
            return
        elif array[meio] < numero:
            inicio = meio + 1 # procura na direita
        else:
            fim = meio - 1 # procura na esquerda
      
    print("Numero nao encontrado no array")


if __name__ == '__main__':
    inicio = time.time()
    array = criar_array()
    print("\n")
    busca_binaria(array)

    fim = time.time()

    tempo_execucao = fim - inicio
    print(f"O tempo de execução foi: {tempo_execucao} ms")