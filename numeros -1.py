#Utilize uma estrutura de repetição para repetir a leitura de todos os números passados como entrada, até que encontre o valor '-1'.
# Ou seja, o número -1 será o critério de parada para a leitura dos dados de entrada.
# Utilize o comando int(input()) para obter todos os números inteiros de entrada. ok
# Calcule a soma de todos os números.
# Mostre na tela a soma calculada, usando o comando print().



soma = 0
numero = int(input())
while (numero != -1):
  soma += numero
  numero = int(input())
print(soma)

