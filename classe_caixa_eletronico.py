class CaixaEletronico:
    
    notas_disponiveis = [100, 50, 20, 10]  # notas disponíveis no caixa eletrônico
    
    def sacar(self, valor):
        notas_entregues = []
        for nota in self.notas_disponiveis:
            while valor >= nota:
                notas_entregues.append(nota)
                valor -= nota
        if valor == 0:        
            return notas_entregues
        elif valor < 10 or valor % 10 != 0:
            return 'valor inválido'
        else:
            return None
        
'''Para utilizar a classe, basta instanciá-la e chamar o método sacar informando o valor a ser sacado, por exemplo:'''

caixa1 = CaixaEletronico()
valor_saque = int(input("Digite o valor a ser sacado: "))
notas_entregues = caixa1.sacar(valor_saque)

if notas_entregues is not None:
    print(notas_entregues)

'''Exemplo de uma segunda instancia da classe caixa eletronico'''

caixa2 = CaixaEletronico()
valor_saque = 370
notas_entregues = caixa2.sacar(valor_saque)
if notas_entregues is not None:
    print(notas_entregues)