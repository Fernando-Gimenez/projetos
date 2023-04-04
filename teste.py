class Cachorro():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def latir(self):
        print("Au au!")
    def raca(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")
        
pitbull = Cachorro("Rex", 5)

pitbull.latir()
pitbull.raca()






