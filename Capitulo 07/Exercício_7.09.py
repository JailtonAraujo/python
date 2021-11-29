# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 7.9 Modifique o Programa 7.2 para utilizar listas de strings para desenhar
#o boneco da forca. Você pode utilizar uma lista para cada linha e organ izá-las em
#uma lista de listas. Em vez de controlar quando imprimir cada parte, desenhe nessas listas, substituindo o elemento a desenhar.

palavras = [
          "java",
          "python",
          "ruby",
          "html",
          "css",
          "javascripth",
          "php"
     ]

índice = int(input("Digite um numero:"))
palavra = palavras[ (índice * 776) % len(palavras)]

for x in range(100):
     print()
digitadas = []
acertos = []
erros = 0

linhas_txt = """
X==:==
X  :
X
X
X
X
=======

"""

linhas = []

for linha in linhas_txt.splitlines():
     linhas.append(list(linha))

while True:
     senha = ""
     for letra in palavra:
         senha += letra if letra in acertos else "."
     print(senha)
     if senha == palavra:
         print("Você acertou!")
         break
     tentativa = input("\nDigite uma letra:").lower().strip()
     if tentativa in digitadas:
         print("Você já tentou esta letra!")
         continue
     else:
         digitadas += tentativa
         if tentativa in palavra:
               acertos += tentativa
         else:
               erros += 1
               print("Você errou!")
               if erros == 1:
                    linhas[3][3] = "O"
               elif erros == 2:
                    linhas[4][3] = "|"
               elif erros == 3:
                    linhas[4][2] = "\\"
               elif erros == 4:
                    linhas[4][4] = "/"
               elif erros == 5:
                    linhas[5][2] = "/"
               elif erros == 6:
                    linhas[5][4] = "\\"

     for l in linhas:
          print("".join(l))
     if erros == 6:
         print("Enforcado!")
         print("A palavra secreta era: %s" % palavra)
         break