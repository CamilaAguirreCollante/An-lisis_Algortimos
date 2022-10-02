"""
    Autores: 
        María Camila Aguirre Collante
        Jessica Tatiana Naizaque Guevara
"""
import copy
from operator import truediv
import random
from tabnanny import check
from colorama import *

init(autoreset=True)
#definir colores que serán usados
yellow = Back.YELLOW
blue = Back.BLUE
red = Back.RED
green = Back.GREEN
cyan = Back.CYAN
purple = Back.MAGENTA
white = Back.WHITE

''' elegir de manera aleatoria el nivel a jugar
@Entradas -> dim: dimensiones del tablero que se desea jugar
@Salidas -> numBoard: número de tablero a jugar
'''
def randomLevel(dim):
    if dim == 9:
        numBoard = random.randint(1, 7)
    else:
        numBoard =  random.randint(1, 10)
    #end if
    return numBoard
#end def

''' Retornar la ruta apropiada para la creación de tableros
'''
def pathC(dim, level, action):
    if action == 'C':
        path = "Niveles" + str(dim) + "X" + str(dim) + "/" + str(level) + ".txt"
    elif action == 'S':
        path = "SoluciónN" + str(dim) + "X" + str(dim) + "/" + str(level) + ".txt"
    #end if
    return path
#end def

''' creación del tablero de juego
@Entradas -> name: nombre del del archivo que se leerá
@Salida -> board: tablero de juego
'''
def createBoard(name):
    board = []
    with open(name, "r") as file:
        for lines in file:
            board.append(lines.split())
        #end for
    return board
#end def

''' creación tablero solucionado
@Entradas
@Salidas
'''

'''
@Entradas -> board=tablero de juego
@Salida -> mostrar el tablero de juego
'''
def showBoard(board):
    boardTemp = copy.deepcopy(board)
    print("-"*(7 * len(boardTemp)+1))
    for i in range(len(boardTemp)):
        for j in range(len(boardTemp)):
            if boardTemp[i][j] == "R" or boardTemp[i][j] == "R!":
                boardTemp[i][j]= str(i)+str(j)
                print("| ", end = "")
                print(red + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "G" or boardTemp[i][j] == "G!":
                boardTemp[i][j]= str(i)+str(j)
                print("| ", end = "")
                print(green + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "B" or boardTemp[i][j] == "B!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(blue + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "Y" or boardTemp[i][j] == "Y!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(yellow + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "W" or boardTemp[i][j] == "W!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(white + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "C" or boardTemp[i][j] == "C!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(cyan + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "P" or boardTemp[i][j] == "P!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(purple + " {:3}".format(boardTemp[i][j]), end = " ")
            else:
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(Back.BLACK + " {:3}".format(boardTemp[i][j]), end = " ")
            #end if
        #end for
        print("|")
        print("-"*(7 * len(boardTemp)+1))
    #end for
#end def

'''
@Entradas ->
@Salida -> 
'''
def checkWinner(board, boardSolved):
    n = len(board)
    counter = 0
    for i in range (n):
        for j in range (n):
            if board[i][j] == boardSolved[i][j]:
                counter += 1
            #end if
        #end for
    #end for
    if counter == (n*n):
        return True
    else:
        return False
    #end if
#end def

'''
@Entradas ->
@Salida -> 
'''
def checkFinished(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "0":
                return False    
            #end if
        #end for
    #end for
    return True
#end def

'''
@Entradas ->
@Salida -> 
'''
def checkBox(board, color, coordenate):
    i = int(coordenate[0])
    j = int(coordenate[1])
    n = len(board)
    if board[i][j] == "0" or "!" not in board[i][j]:
        if i > 0:
            if board[i-1][j] == color or board[i-1][j] == color+"!": #Si su casilla de arriba es del mismo color
                return True
            #end if
        #end if
        if j > 0:
            if board[i][j-1] == color or board[i][j-1] == color+"!": #Si su casilla izquierda es del mismo color
                return True
            #end if
        #end if
        if i < n-1:
            if board[i+1][j] == color or board[i+1][j] == color+"!": #Si su casilla de abajo es del mismo color
                return True
            #end if
        #end if
        if j < n-1:
            if board[i][j+1] == color or board[i][j+1] == color+"!": #Si su casilla derecha es del mismo color
                return True
            #end if
        #end if
        print("******No hay casillas adyacentes del color seleccionado.\n")
    if "!" in board[i][j]:
        print("******No puede cambiar una casilla inicial.\n")
    #end if
    return False
#end def

'''
@Entradas ->
@Salida -> 
'''
def selectMove(board, boardS):
    finished = False #Verificar que el juego no haya finalizado (cuando todas las casillas tienen color)
    win = False
    while not finished:
        parameters = False #Verificar que los parámetros estén correctos y que haya seleccionado una casilla correcta
        while not parameters:
            print("Recuerde que los colores son:  ", red + " {:4}".format("Red"), green + " {:6}".format("Green"), blue + " {:5}".format("Blue"), yellow + " {:7}".format("Yellow"), white + " {:6}".format("White"), cyan + " {:5}".format("Cyan"), purple + " {:7}".format("Purple"), end = " ")
            print("\n")
            move = str(input("Digite la inicial del color que desea utilizar y la casilla que desea jugar (Ej: R 34): "))
            movements = move.split()
            if len(movements) == 2:
                if movements[0].isalpha():
                    if movements[1].isnumeric():
                        if movements[0].upper() == "R" or movements[0].upper() == "G" or movements[0].upper() == "B" or movements[0].upper() == "Y" or movements[0].upper() == "W" or movements[0].upper() == "C" or movements[0].upper() == "P": 
                            if len(movements[1])  == 2:
                                if (int(movements[1][0]) >= 0) and (int(movements[1][0]) < len(board)) and (int(movements[1][1]) >= 0) and (int(movements[1][1]) < len(board)):
                                    parameters = checkBox(board, movements[0].upper(), movements[1])
                                    #Verificar que no tenga más de dos adyacentes
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
        board[int(movements[1][0])][int(movements[1][1])] = movements[0].upper()
        showBoard(board)
        finished = checkFinished(board)
        #print(finished)
        if finished:
            win = checkWinner(board, boardS)
            if win == False:
                finished = False
                print("\t\tNo ha completado de manera correcta el nivel :(")
                print("\t\t\t\nPor favor, siga intentando :D")
            else:
                finished = True
                print("\t\tHa superado el nivel con éxito! ")
            #end if
        #end if
    #end while
#end def