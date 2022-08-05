import  random
def jogar():
    imprime_mensagem_abertura()
    tema = escolhe_tema()
    palavra_secreta = carrega_palavra_secreta(tema)
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    vidas = 7
    while(not acertou and not enforcou):
        chute = pede_chute()
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            vidas -= 1
            desenha_forca(vidas)
        print(letras_acertadas)

        enforcou = vidas == 0
        acertou = "_" not in letras_acertadas


    imprime_resultado(acertou,palavra_secreta)

# Funções
def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def escolhe_tema():
    temas = ("frutas","times","cidades","esportes")
    i = 0
    print("Temas")
    for i in range(len(temas)):
        print(i+1, temas[i])
    tema = int(input("Digite o número de qual tema você deseja jogar : "))
    while(tema<0 or tema>len(temas)):
        print("Tema inválido, selecione novamente...")
        tema = input("Digite o número de qual tema você deseja jogar : ")
    return temas[tema-1]



def carrega_palavra_secreta(tema):
    arquivo = open("modos/{}.txt".format(tema), "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    palavra_escondida = []
    i = 0
    for i in range(len(palavra)):
        if (" " == palavra[i]):
            palavra_escondida.append(" ")
        else:
            palavra_escondida.append("_")
    return palavra_escondida


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_resultado(acertou,palavra_secreta):
    if(acertou):
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
    else:
        print("Poxa, você foi enforcado!")
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



def desenha_forca(vidas):
    print("  _______     ")
    print(" |/      |    ")

    if(vidas == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(vidas == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(vidas == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(vidas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(vidas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(vidas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (vidas == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



if(__name__ ==  "__main__"):
    jogar()
