print("*****************")
print("Bem vindo ao jogo")
print("*****************")

numero = 45

# recebe o número (string) pelo teclado
chute_string = input("Forneca o numero: ")

# converte string em inteiro
chute = int(chute_string)

if(numero == chute):
    print("Voce acertou !!")
else:
    print("Voce errou !!!")

print("Jogo terminado")

