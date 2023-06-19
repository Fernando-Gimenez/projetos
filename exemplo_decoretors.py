
def imprima_os_parametros(func):
    def decorator_imprimir (capital, taxa, tempo):
        resultado = func(capital, taxa, tempo)
        print('resultado', resultado )
        return resultado
    return decorator_imprimir
   
        

@imprima_os_parametros
def juros_simples(capital, taxa, tempo):
    resultado =  capital *(taxa / 100) * tempo
    return resultado


juros_simples(1000, 5, 6)

