# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 9.36 Utilizando a função os. wa lk, crie um programa que calcule o espaço
#ocupado por cada diretório e -subdiretório, gerando uma página html com os
#resultados.

import sys
import os
import os.path
import math

def tamanho_para_humanos(tamanho):
    if tamanho == 0:
        return "0 byte"
    grandeza = math.log(tamanho, 10)
    if grandeza < 3:
        return f"{tamanho} bytes"
    elif grandeza < 6:
        return f"{tamanho / 1024.0:7.3f} KB"
    elif grandeza < 9:
        return f"{tamanho / pow(1024, 2)} MB"
    elif grandeza < 12:
        return f"{tamanho / pow(1024, 3)} GB"


mascara_do_estilo = "'margin: 5px 0px 5px %dpx;'"


def gera_estilo(nível):
    return mascara_do_estilo % (nível * 30)


# Retorna uma função, onde o parâmetro nraiz é utilizado
# para calcular o nível da identação
def gera_nível_e_estilo(raiz):
    def nivel(caminho):
        xnivel = caminho.count(os.sep) - nraiz
        return gera_estilo(xnivel)
    nraiz = raiz.count(os.sep)
    return nivel


# Usa a os.walk para percorrer os diretórios
# E uma pilha para armazenar o tamanho de cada diretório
def gera_listagem(página, diretório):
    diretório = os.path.abspath(diretório)
    # identador é uma função que calcula quantos níveis
    # a partir do nível de diretório um caminho deve possuir.
    identador = gera_nível_e_estilo(diretório)
    pilha = [[diretório, 0]]  # Elemento de guarda, para evitar pilha vazia
    for raiz, diretórios, arquivos in os.walk(diretório):
        # Se o diretório atual: raiz
        # Não for um subdiretório do último percorrido
        # Desempilha até achar um pai comum
        while not raiz.startswith(pilha[-1][0]):
            último = pilha.pop()
            página.write(f"<p style={identador(último[0])}>Tamanho: (tamanho_para_humanos(último[1]))</p>")
            pilha[-1][1] += último[1]
        página.write(f"<p style={identador(raiz)}>{raiz}</p>")
        d_tamanho = 0
        for a in arquivos:
            caminho_completo = os.path.join(raiz, a)
            d_tamanho += os.path.getsize(caminho_completo)
        pilha.append([raiz, d_tamanho])
    # Se a pilha tem mais de um elemento
    # os desempilha
    while len(pilha) > 1:
        último = pilha.pop()
        página.write(f"<p style={identador(último[0])}>Tamanho: ({tamanho_para_humanos(último[1])})</p>")
        pilha[-1][1] += último[1]


if len(sys.argv) < 2:
    print("Digite o nome do diretório para coletar os arquivos!")
    sys.exit(1)

diretório = sys.argv[1]

página = open("tarquivos.html", "w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Arquivos</title>
</head>
<body>
""")
página.write(f"Arquivos encontrados a partir do diretório: {diretório}")
gera_listagem(página, diretório)
página.write("""
</body>
</html>
""")
página.close()