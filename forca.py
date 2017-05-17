def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not acertou and not enforcou):

        chute = input("Digite a nova letra: ")

        index = 0;
        # percorre cada letra da palavra secreta
        for letra in palavra_secreta :
            index += 1
            if(letra == chute):
                print("posição:", index, "letra", letra)



    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
