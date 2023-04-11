from PIL import Image

# Abrir a imagem
imagem = Image.open(r"C:\Users\Fernando Gimenez\Desktop\WO\Alignment_Grid.png")

# Mostrar informações da imagem
print(imagem.format)
print(imagem.size)
print(imagem.mode)

# Exibir a imagem
imagem.show()



