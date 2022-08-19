from random import randint 
rejogo = "S"
palavras_listadas = ["arroz", "feijao", "batata", "computador", "carro", "inconstitucionalissimamente", "pedra", "rocha"]
comprimento_lista = len(palavras_listadas) - 1
placar = 0 
while rejogo == "S" or rejogo == "SIM":
    erros = 0
    palavra_secreta = ""
    letras_jogadas = []
    letra_jogada = ""
    palavra_secreta = palavras_listadas[randint(0,comprimento_lista)].upper()
    palavra_jogada = "*"*len(palavra_secreta)
    while erros < 3:
        print("-"*50)
        print(f"Erros: {erros}")
        print("\nPALAVRA SECRETA: ")
        print(f"{palavra_jogada}")
        print(f"\nLETRAS JOGADAS {letras_jogadas}")
        palavra_jogada = ""
        letra_jogada = input("\nDigite uma letra: ").upper()
        while letra_jogada in letras_jogadas:
            print(f"\nVocê já jogou a letra {letra_jogada}")
            letra_jogada = input("Digite uma letra: ").upper()
        letras_jogadas.append(letra_jogada)
        if letra_jogada not in palavra_secreta:
            erros +=1
            print("-"*50)
            print(f"\n \033[1;49;31mVOCÊ ERROU, A LETRA {letra_jogada} NÃO ESTÁ NA PALAVRA SECRETA\n\033[1;97m ")
        for l in palavra_secreta:
            if l in letras_jogadas:
                palavra_jogada +=f"{l}"
            else:
                palavra_jogada +="*"
        if palavra_jogada.upper() == palavra_secreta:
            print(f"\nPARABÉNS, VOCÊ ACERTOU A PALAVRA SECRETA! --------> {palavra_secreta}")
            placar +=1
            print(f"\n SEU PLACAR AGORA ESTÁ COM {placar} PONTO(S)")
            break
    if erros == 3:
        print(f"\nGAME OVER! A PALAVRA SECRETA ERA {palavra_secreta}")
        print(f"\n SEU PLACAR AGORA ESTÁ COM {placar} PONTO(S)")

    rejogo = input("Deseja jogar novamente? [S] Sim ou [N] Não ----> ").upper()


    