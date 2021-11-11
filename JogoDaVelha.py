resp = 's'
while resp == 's':
    linha_0 = [' ',' ',' ']
    linha_1 = [' ',' ',' ']
    linha_2 = [' ',' ',' ']

    matriz = [linha_0,linha_1,linha_2]
    rodada = 0

      
    def jogadorUm():
        
        while True:
            print(' ')
            print(f'Vez de: {nomeJogUm} ')
                
            lin = int(input('N° da Linha: '))
            col = int(input('N° da Coluna: '))
          
            if(matriz [lin][col] == ' '):
                matriz [lin][col] = jogUm
                break
            else:
                print('Jogada Inválida')
     


    def jogadorDois():
        
        while True:
            print(' ')
            print(f'Vez de: {nomeJogDois}')

            lin = int(input('N° da Linha: '))
            col = int(input('N° da Coluna: '))
         
            if(matriz [lin][col] == ' '):
                matriz [lin][col] = jogDois
                break
            else:
                print('Jogada Inválida')
            

        
    def juiz ():
            vencedor = ''
            
            #CHECK LINHA
            if (matriz[0][0] == matriz[0][1] == matriz[0][2] == jogUm or matriz[1][0] == matriz[1][1] == matriz[1][2] == jogUm or matriz[2][0] == matriz[2][1] == matriz[2][2] == jogUm):
                print(f'{nomeJogUm} venceu!')
                vencedor =  jogUm
                
            #CHECK COLUNA
            elif(matriz[0][0] == matriz[1][0] == matriz[2][0] == jogUm or matriz[0][1] == matriz[1][1] == matriz[2][1] == jogUm or matriz[2][0] == matriz[2][1] == matriz[2][2] == jogUm ):
                print(f'{nomeJogUm} venceu!')
                vencedor =  jogUm
                
            #CHECK DIAGONAL
            elif(matriz[0][0] == matriz[1][1] == matriz[2][2] == jogUm or matriz[0][2] == matriz[1][1] == matriz[2][0] == jogUm):
                print(f'{nomeJogUm} venceu!')
                vencedor =  jogUm
                
            #CHECK LINHA
            elif (matriz[0][0] == matriz[0][1] == matriz[0][2] == jogDois or matriz[1][0] == matriz[1][1] == matriz[1][2] == jogDois or matriz[2][0] == matriz[2][1] == matriz[2][2] == jogDois):
                print(f'{nomeJogDois} venceu!')
                vencedor =  jogDois
                
            #CHECK COLUNA
            elif(matriz[0][0] == matriz[1][0] == matriz[2][0] == jogDois or matriz[0][1] == matriz[1][1] == matriz[2][1] == jogDois or matriz[2][0] == matriz[2][1] == matriz[2][2] == jogDois ):
                print(f'{nomeJogDois} venceu!')
                vencedor =  jogDois
                
            #CHECK DIAGONAL
            elif(matriz[0][0] == matriz[1][1] == matriz[2][2] == jogDois or matriz[0][2] == matriz[1][1] == matriz[2][0] == jogDois):
                print(f'{nomeJogDois} venceu!')
                vencedor =  jogDois
           
            return vencedor
       
  
    while True:    
        if(rodada == 0):
            nomeJogUm = str(input('Nome do Jogador UM --> '))
            nomeJogDois = str(input('Nome do Jogador Dois --> '))
            print('-----------------------------')
            jogUm = str(input(f'Jogador UM ({nomeJogUm}) [o][x]: '))
            
            if (jogUm == 'x'):
                jogDois = 'o'
                print(f'Jogador DOIS ({nomeJogDois}) será [o]')
                
            elif (jogUm == 'o'):
                jogDois = 'x'
                print('Jogador DOIS ({nomeJogDois}) será [x]')


        print(' ')
        jogadorUm()
        print(linha_0)
        print(linha_1)
        print(linha_2)
        juiz()
        rodada += 1
        
        if(juiz() == jogUm):
            break
        elif (juiz() == '') and (rodada >= 9):
             print('velha')
             break
        
        jogadorDois()
        print(linha_0)
        print(linha_1)
        print(linha_2)
        juiz()
        rodada += 1
        
        if(juiz() == jogDois):
            break
        elif (juiz() == '') and (rodada >= 9):
            print('Velha!')
            break

    resp = input('Jogar novamente? (s/n): ')
    if (resp == 'n'):
        print('finalizado!')
        break
    else:
        pass
    
