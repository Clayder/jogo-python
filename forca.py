import random

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def pede_chute():
   chute = input("Digite a nova letra: ")
   chute = chute.strip().upper()
   return chute

def carrega_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        # retira o \n da linha
        linha = linha.split()

        # adiciona a palavra no inicio da lista
        palavras.append(linha)

    arquivo.close()

    return palavras

def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    mensagem_abertura()

    # carrega as palavras do arquivo
    palavras = carrega_palavras()

    # sorteia um número entre 0 e o tamanho da lista
    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero][0].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = True
    erros = 0

    while (acertou and not enforcou):

        # recebe a palavra do jogador
        chute = pede_chute()

        acertei_chute = False
        index = 0;

        # percorre cada letra da palavra secreta
        for letra in palavra_secreta:
            index += 1
            if (letra == chute):
                print("posição:", index, "letra", letra)
                letras_acertadas[index - 1] = letra
                # recebe verdadeiro ou falso se ainda existir lacunas
                acertou = "_" in letras_acertadas
                acertei_chute = True

        erros = erros if acertei_chute else (erros + 1)

        desenha_forca(erros)

        enforcou = erros == 7

        print(letras_acertadas)
        print()

    if(enforcou):
        desenha_forca(erros)
        imprime_mensagem_perdedor(palavra_secreta)
    if(not acertou):
        imprime_mensagem_vencedor()

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
