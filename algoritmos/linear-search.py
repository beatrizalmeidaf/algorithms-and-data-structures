import time

def criar_array():
    array = []
    size = int(input("Qual o tamanho do seu array?\n"))

    for i in range(size):
        elemento = input("Insira os numeros do array\n")
        array.append(int(elemento))

    return array

def busca_linear(array):
    numero = int(input("Qual numero deseja buscar?\n"))

    for i in range(len(array)):
        if numero == array[i]:
            print("Numero encontrado no array!")
            return
      
    print("Numero nao encontrado no array")



if __name__ == '__main__':
    inicio = time.time()
    array = criar_array()
    busca_linear(array)
    fim = time.time()

    tempo_execucao = fim - inicio
    print(f"O tempo de execução foi: {tempo_execucao} ms")