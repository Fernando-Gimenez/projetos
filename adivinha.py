from random import randint

#numero randomico de 1 a 10
numero = randint(1, 50)

#numero de tentativas 
tentativas = 3
#enquanto um numero maior que 0, chute um numero inteiro (int) se o chute for igual ao nuimero randomico (randit) imprima parabéns!
while tentativas > 0:
    chute = int(input('numero do chute'))
    diferenca = numero - chute
    if chute == numero:
        print('parabéns') 
        break 
    elif diferenca <= 5 and diferenca >= -5:
        print('vc está perto')    
    else:
        print('errou')   
    tentativas = tentativas -1
print('fim o numero era:', numero)    








