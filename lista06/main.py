import numpy as np
import math

#Abrir o arquivo original e a cópia
entrada = open("balao.ppm", "r+")
saida = open("balao_copia.ppm", "w+")

linha = entrada.readline() #P3
linha = entrada.readline() #Comentário
linha = entrada.readline() #Dimensões
dimensoes = linha.split()
largura = int(dimensoes[0])
altura = int(dimensoes[1])
linha = entrada.readline() #Valor fixo
linha = entrada.readlines() #Ler o restante do arquivo e grava como lista

#converter de lista para array
imagem = np.asarray(linha, dtype=int)
#reshape
imagem = np.reshape(imagem, (altura, largura, 3))

#Escrevendo a imagem cópia
saida.write("P3\n")
saida.write("#Criado por Andre\n")
saida.write(str(largura))
saida.write(" ")
saida.write(str(altura))
saida.write("\n")
saida.write("255\n")

#Fazer a cópia com transformações
for i in range(len(imagem)):
    for j in range(len(imagem[1])):
        for k in range(3):
            sum = imagem[i][j][k]
            sum = str(sum)
            saida.write(sum)
            saida.write("\n")

#Fechar os dois arquivos
entrada.close()
saida.close()
