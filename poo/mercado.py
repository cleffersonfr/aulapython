class Pessoa():

    def __init__(self,nome,idade):# metodo
        self.nome = nome # self.variavel -> atributo da classe
        self.idade = idade

    def faz_aniversario(self):
        self.idade+=1


class Produto():

    def __init__(self,id,nome,preco,categoria,peso):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.peso = peso

    def mostra_dados(self):
        print(f"Produto: {self.nome}-{self.id}\nPreco: {self.preco:.2f}")

class Item():
    qtd_itens =0

    def __init__(self,produto,qtd):
        qtd_items+=1
        self.id = qtd_items
        self.produto = produto
        self.qtd = qtd



class Carrinho():
  
    
    def __init__(self,id):
        
        self.id = id
        self.items = []
      

    def adicionar_produto(self,produto,qtd):
        item = Item(produto,qtd)
        self.items.append(produto)

    def remover_produto(self,produto_id):
        for i  in range(self.items):
            produto = self.items[i].produto
            if produto.id == produto_id:
                self.items.pop(i)
                produto.mostra_dados()
                print(f"Removido!")

    def get_valor_total(self):
        valor_total = 0
        for item in self.items:
            valor_total = valor_total + item.produto.preco
        return valor_total

    def mostra_valor(self):
        print("Valor Total:" ,self.get_valor_total(self))

        
    

