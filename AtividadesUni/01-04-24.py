'''  
Defina como o seu time o cenário de aplicação para o projeto
O projeto deve atendes os seguintes requisitos:
- Criar a própria lista (classe e métodos).
- Atender as classes no e lista (ver abaixo). O time deve adaptar as propriedades da classe, conforme o cenario definido para o projeto

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
    def mostrar_no(self):
        print(self.valor)
        
class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        
- Utilizar o seguinte conjunto mínimo de métodos: inclusão, exclusão, consulta e relatório. 
'''
class No:
    def __init__(self, item, quantidade=1):
        self.item = item
        self.quantidade = quantidade
        self.proximo = None
        
    def mostrar_no(self):
        print(f"{self.quantidade}x {self.item}")

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        
    def incluir_item(self, item, quantidade=1):
        novo_no = No(item, quantidade)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
            
    def excluir_item(self, item):
        atual = self.primeiro
        anterior = None
        while atual:
            if atual.item == item:
                if anterior is None:
                    self.primeiro = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return  # Item excluído, saímos da função
            anterior = atual
            atual = atual.proximo
        print("Item não encontrado na lista.")
        
    def consultar_item(self, item):
        atual = self.primeiro
        while atual:
            if atual.item == item:
                return atual
            atual = atual.proximo
        return None  # Item não encontrado na lista
    
    def relatorio(self):
        atual = self.primeiro
        if atual is None:
            print("Lista de compras vazia.")
        else:
            print("Lista de compras:")
            while atual:
                atual.mostrar_no()
                atual = atual.proximo
