from ChessBoard import Board


class util():
    def __init__(self):
        pass

    def converter_inputs(self,input):
        novo_local_provisorio = input[0] + input[1]
        novo_local = 0
        if novo_local_provisorio[0] == "a":
            novo_local += 1
        elif novo_local_provisorio[0] == "b":
            novo_local += 2
        elif novo_local_provisorio[0] == "c":
            novo_local += 3
        elif novo_local_provisorio[0] == "d":
            novo_local += 4
        elif novo_local_provisorio[0] == "e":
            novo_local += 5
        elif novo_local_provisorio[0] == "f":
            novo_local += 6
        elif novo_local_provisorio[0] == "g":
            novo_local += 7
        elif novo_local_provisorio[0] == "h":
            novo_local += 8
            novo_local += (int(novo_local_provisorio[1]) - 1) * 8
        return novo_local
    

    #AJEITAR OS MOVIMENTOS DAS PEÇAS PARA DEPOIS AJEITAR A FUNÇÃO TODOS_OS_MOVIMENTOS_POSSIVEIS#
    
    
    
    
    
    
    
    def peca_ameacada(self,local_atual):
        cor_do_jogador_adversario = ""
        if self.gameTiles[local_atual].count("Pretas") == 1:
            cor_do_jogador_adversario = "Brancas"
        else:
            cor_do_jogador_adversario = "Pretas"
        if local_atual in a.todos_os_movimentos_possiveis(cor_do_jogador_adversario,self.gameTiles):
            return 1
        else:
            return 0
        mov_possiveis = a.todos_os_movimentos_possiveis("Brancas",self.gameTiles) + a.todos_os_movimentos_possiveis("Pretas",self.gameTiles)
        if self.gameTiles[local_atual] == "" and (local_atual in mov_possiveis):
            return 1
        else:
            return 0


