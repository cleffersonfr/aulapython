# classe  -> conjunto de variaveis e funcoes 
#Objeto e uma instancia de classe

class Pessoa():

    def __init__(self,nome,idade):# metodo
        self.nome = nome # self.variavel -> atributo da classe
        self.idade = idade

    def faz_aniversario(self):
        self.idade+=1

class Aluno(Pessoa):
    def __init__(self, nome, idade,escola):
        super().__init__(nome, idade)
        self.escola = escola


p1 = Pessoa(nome="Marcus",idade=23)
p2 = Pessoa("Clecle",10)
a1 = Aluno("joao",20,"ARi de sa")

p1.faz_aniversario()
p2.faz_aniversario()

print(p1.nome)
print(p2.idade)