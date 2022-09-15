"""
    Autores: 
        María Camila Aguirre Collante
        Jessica Tatiana Naizaque Guevara
"""
import copy
from colorama import *
#from termcolor import colored, cprint

init(autoreset=True)
#definir colores que serán usados
yellow = Back.YELLOW
blue = Back.BLUE
red = Back.RED
green = Back.GREEN
cyan = Back.CYAN
purple = Back.MAGENTA
white = Back.WHITE

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
@Salida -> ubica los colores iniciales
'''
def initialBoard(board):
    boardTemp = copy.deepcopy(board)
    dim = len(boardTemp)
    if dim == 5:
        boardTemp[0][0] = "R"
        boardTemp[4][1] = "R"
        boardTemp[0][2] = "G"
        boardTemp[3][1] = "G"
        boardTemp[1][2] = "B"
        boardTemp[4][2] = "B"
        boardTemp[3][3] = "Y"
        boardTemp[0][4] = "Y"
        boardTemp[4][3] = "W"
        boardTemp[1][4] = "W"
    elif dim == 6:
        boardTemp[0][0] = "G"
        boardTemp[4][0] = "G"
        boardTemp[5][0] = "Y"
        boardTemp[0][1] = "Y"
        boardTemp[0][2] = "C"
        boardTemp[2][2] = "C"
        boardTemp[0][4] = "R"
        boardTemp[3][2] = "R"
        boardTemp[1][4] = "W"
        boardTemp[4][2] = "W"
        boardTemp[0][5] = "B"
        boardTemp[5][2] = "B"
    for i in range(len(boardTemp)):
        for j in range(len(boardTemp)):
            if boardTemp[i][j] == 0:
                boardTemp[i][j] = " "
            #end-if
        #end-for
    #end-for
    return boardTemp

def showBoard(board):
    boardTemp = initialBoard(board)
    print("-"*(7 * len(boardTemp)+1))
    for i in range(len(boardTemp)):
        for j in range(len(boardTemp)):
            if boardTemp[i][j]=="R":
                boardTemp[i][j]=" "
                print("| ", end = "")
                print(red + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="G":
                boardTemp[i][j]=" "
                print("| ", end = "")
                print(green + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="B":
                boardTemp[i][j]=" "
                print("| ", end = "")
                print(blue + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="Y":
                boardTemp[i][j]=" "
                print("| ", end = "")
                print(yellow + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="W":
                boardTemp[i][j]=" "
                print("| ", end = "")
                print(white + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="C":
                boardTemp[i][j]=" "
                print("| ", end = "")
                print(cyan + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="P":
                boardTemp[i][j]=" "
                print("| ", end = "")
                print(purple + " {:3}".format(boardTemp[i][j]), end = " ")
            else:
                print("| {:4}".format(boardTemp[i][j]), end = " ")
        #end-for
        print("|")
        print("-"*(7 * len(boardTemp)+1))
    #end-for
#end-def

