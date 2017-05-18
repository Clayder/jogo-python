def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ['_','_','_','_','_','_']

    print(palavra_secreta.count())

    enforcou = False
    acertou = False

    while (not acertou and not enforcou):

        chute = input("Digite a nova letra: ")
        chute = chute.strip()

        index = 0;
        # percorre cada letra da palavra secreta
        for letra in palavra_secreta :
            index += 1
            if(letra.upper() == chute.upper()):
                print("posição:", index, "letra", letra)
                letras_acertadas[index - 1] = letra

        print(letras_acertadas)
        print()

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
