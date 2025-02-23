class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]  # lista de listas

    def _hash(self, chave):
        return hash(chave) % self.tamanho  # gera um índice

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                par = (chave, valor)  # atualiza valor se a chave já existir
                return
        self.tabela[indice].append((chave, valor))  # adiciona novo par

    def buscar(self, chave):
        indice = self._hash(chave)
        for k, v in self.tabela[indice]:
            if k == chave:
                return v
        return None  

    def remover(self, chave):
        indice = self._hash(chave)
        for i, par in enumerate(self.tabela[indice]):
            if par[0] == chave:
                del self.tabela[indice][i]  # remove o par encontrado
                return True
        return False  


tabela = TabelaHash()
tabela.inserir("nome", "Beatriz")
tabela.inserir("idade", 25)
print(tabela.buscar("nome")) 
print(tabela.buscar("idade"))  
tabela.remover("nome")
print(tabela.buscar("nome"))  
