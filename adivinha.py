from random import randint

numero = randint(1, 10)

tentativas = 5
while tentativas > 0:
    chute = int(input('numero do chute'))
    diferenca = numero - chute
    if diferenca == numero:
        print('parabéns') 
        break  
    else:
        print('errou')
    tentativas = tentativas -1









