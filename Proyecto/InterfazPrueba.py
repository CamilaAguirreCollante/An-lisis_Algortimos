"""
    Autores: 
        María Camila Aguirre Collante
        Jessica Tatiana Naizaque Guevara
"""
import copy
from operator import truediv
from tabnanny import check
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
                boardTemp[i][j]= str(i)+str(j)
                print("| ", end = "")
                print(red + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="G":
                boardTemp[i][j]= str(i)+str(j)
                print("| ", end = "")
                print(green + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="B":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(blue + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="Y":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(yellow + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="W":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(white + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="C":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(cyan + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j]=="P":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(purple + " {:3}".format(boardTemp[i][j]), end = " ")
            else:
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(Back.BLACK + " {:3}".format(boardTemp[i][j]), end = " ")
                #print("| {:4}".format(boardTemp[i][j]), end = " ")
        #end-for
        print("|")
        print("-"*(7 * len(boardTemp)+1))
    #end-for
#end-def

def check_finished(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return False    
            #end if
        #end for
    #end for
    return True
#end def


def select_move(board):
    finished = False
    parameters = False
    while not finished:
        finished = check_finished(board)
        print(finished)
        while not parameters:
            print("Recuerde que los colores son:  ", red + " {:4}".format("Red"), green + " {:6}".format("Green"), blue + " {:5}".format("Blue"), yellow + " {:7}".format("Yellow"), white + " {:6}".format("White"), cyan + " {:5}".format("Cyan"), purple + " {:7}".format("Purple"))
            move = str(input("Digite la inicial del color que desea utilizar y la casilla que desea jugar (Ej: R 34): "))
            movements = move.split()
            if len(movements) == 2:
                if movements[0].isalpha():
                    if movements[1].isnumeric():
                        if movements[0].upper() == "R" or movements[0].upper() == "G" or movements[0].upper() == "B" or movements[0].upper() == "Y" or movements[0].upper() == "W" or movements[0].upper() == "C" or movements[0].upper() == "P": 
                            if len(movements[1])  == 2:
                                if int(movements[1][0]) >= 0 and int(movements[1][0]) < len(board) and int(movements[1][1]) >= 0 and int(movements[1][0]) < len(board):
                                    parameters = True
                                else:
                                    print("******Número de casilla incorrecta.\n")
                                #end if
                            else:
                                print("******Número de casilla incorrecta.\n")
                            #end if
                        else:
                            print("******Inicial de color inválida.\n")
                        #end if
                    else:
                        print ("******Parámetro casilla incorrecto.\n")
                    #end if
                else:
                    print ("******Parámetro color incorrecto.\n")
                #end if
            else:
                print("******Cantidad de parámetros enviados incorrecta.\n")
            #end if
        #end while
        #######Continuación del juego
        finished = True #Mientras continuamos el juego para verificar si ya terminó
    #end while
#end def