print("*********************************")
print("Bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

print("Você digitou", chute_str)

chute = int(chute_str)

if numero_secreto != chute:
    print("Você errou")
else:
    print("Voce acertou")

print("Fim do jogo")
