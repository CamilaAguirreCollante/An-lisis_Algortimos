"""
    Autores: 
        María Camila Aguirre Collante
        Jessica Tatiana Naizaque Guevara

                Interfaz Juego Flow Free
    Videojuego que 
"""
import copy
'''
@Entradas -> dim=dimensiones del tablero de juego
@Salida -> creación del tablero de juego
'''
def createBoard(dim):
    board = []
    for i in range(dim):
        board.append([])
        for j in range(dim):
            board[i].append(0)
        #end-for
    #end-for
    return board
#end-def

'''
@Entradas -> tablero de juego 
@Salida -> muestra el tablero de juego
'''
def showBoard(board):
    boardTemp = copy.deepcopy(board)
    for i in range(len(boardTemp)):
        for j in range(len(boardTemp)):
            if boardTemp[i][j] == 0:
                boardTemp[i][j] = " "
            #end-if
        #end-for
    #end-for
    print("-"*(7 * len(boardTemp)+1))
    for i in range(len(boardTemp)):
        for j in range(len(boardTemp)):
            print("| {:4}".format(boardTemp[i][j]), end = " ")
        #end-for
        print("|")
        print("-"*(7 * len(boardTemp)+1))
    #end-for
#end-def
