def computador_escolhe_jogada (n,m):
    if n <= m:
        return n
    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
        else:
            return m

def usuario_escolhe_jogada (n,m):
    peças_tirar = 0
    while peças_tirar == 0:
        peças_tirar = int(input("Quantas peças você vai tirar? "))
        if peças_tirar < 1 or peças_tirar > m:
            print("Oops! Jogada inválida! Tente de novo.")
            peças_tirar = 0
    return peças_tirar
        
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada?"))

    peças_restantes = n
    vez_do_computador = True

    if n % (m+1) == 0:
        vez_do_computador = False
        print("Você começa!\n")
    else:
        print("Computador começa!\n")

    while peças_restantes > 0:
        
        if vez_do_computador == True:
            peças_tirar = computador_escolhe_jogada(peças_restantes,m)
            vez_do_computador = False
            if peças_tirar == 1:
                print ("O computador tirou", peças_tirar, "peça.")
            else:
                print ("O computador tirou", peças_tirar, "peças.")
        else:
            peças_tirar = usuario_escolhe_jogada(peças_restantes,m)
            vez_do_computador = True
            if peças_tirar == 1:
                print ("Você tirou", peças_tirar, "peça.")
            else:
                print ("Você tirou", peças_tirar, "peças.")
        peças_restantes = peças_restantes - peças_tirar
        if peças_restantes == 0:
            print("Não restam mais peças no tabuleiro!\n")
        elif peças_restantes == 1:
            print("Agora resta apenas", peças_restantes, "peça no tabuleiro.\n")
        else:
            print("Agora restam apenas", peças_restantes, "peças no tabuleiro.\n")
    if vez_do_computador:
        print("Fim do jogo! Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 0
                

def campeonato():
    pontos_usuario = 0
    pontos_computador = 0
    aux = 1
    while aux <= 3:
        print("""
**** Rodada""", aux, """ ****
""")
        vencedor = partida()
        if vencedor == 1:
            pontos_usuario += 1
        else:
            pontos_computador += 1
        aux = aux+1
    print("Placar final: você", pontos_usuario, "x", pontos_computador, "computador")
        

tipo_jogo = 0          
while tipo_jogo == 0:
    print('Bem-vindo ao jogo do NIM! Escolha: ')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato ')

    tipo_jogo = int(input(""))

    if tipo_jogo == 1:
        print("Você escolheu uma partida isolada!\n")
        partida()
        break
    elif tipo_jogo == 2:
        print("Você escolheu um campeonato!\n")
        campeonato()
        break
    else:
        print("Opção Inválida!\n")
        tipo_jogo = 0
