def gerar_numeros():
    numero = 1
    while True:
        yield numero
        numero += 1

# Utilizando o gerador para obter os números
meu_gerador = gerar_numeros()
for i in range(100):
    print(next(meu_gerador))

