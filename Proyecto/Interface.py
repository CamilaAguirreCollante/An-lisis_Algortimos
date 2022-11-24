"""
    Autores:
        María Camila Aguirre Collante
        Jessica Tatiana Naizaque Guevara
"""
import copy
import random
from colorama import *

'''Declaración listas necesarias:
        ° xInitial: lista de 'strings' que indican las coordenadas
                    de las posiciones iniciales de 'x' color en el tablero.
        ° pathX: lista de 'strings' que indican las coordenadas del
                 camino correspondiente al color 'X'.
'''
init(autoreset=True)
rInitial = []
bInitial = []
yInitial = []
gInitial = []
wInitial = []
cInitial = []
pInitial = []
pathR = []
pathG = []
pathY = []
pathB = []
pathW = []
pathC = []
pathP = []
#definir colores que serán usados
yellow = Back.YELLOW
blue = Back.BLUE
red = Back.RED
green = Back.GREEN
cyan = Back.CYAN
purple = Back.MAGENTA
white = Back.WHITE
''' Llena cada lista con las posiciones iniciales de cada color.
@Entradas -> board: tablero inicial del juego.
@Salidas -> cada xInitial lleno.
'''
def defInitials(board):
    dim = len(board)
    for i in range(dim):
        for j in range(dim):
            if board[i][j] == "R!":
                rInitial.append(str(i)+str(j))
            elif board[i][j] == "B!":
                bInitial.append(str(i)+str(j))
            elif board[i][j] == "Y!":
                yInitial.append(str(i)+str(j))
            elif board[i][j] == "G!":
                gInitial.append(str(i)+str(j))
            elif board[i][j] == "W!":
                wInitial.append(str(i)+str(j))
            elif board[i][j] == "C!":
                cInitial.append(str(i)+str(j))
            elif board[i][j] == "P!":
                pInitial.append(str(i)+str(j))
            #end if
        #end for
    #end for
#end def
''' Creación del tablero de juego a partir de la elección aleatoria del mismo.
@Entradas -> dim(int): dimensiones del tablero de juego(.
@Salida -> board(list): creación del tablero de juego.
'''
def createBoard(dim):
    if dim < 7:
        numBoard =  random.randint(1, 5)        
    else:
        numBoard =  random.randint(1, 4)
    #end if
    path = "Niveles" + str(dim) + "X" + str(dim) + "/" + str(numBoard) + ".txt"
    #path = "Niveles6X6/5.txt"
    #path = "Niveles8X8/1.txt"
    #path = "Niveles9X9/5.txt"
    board = []
    with open(path, "r") as file:
        for lines in file:
            board.append(lines.split())
        #end for
    defInitials(board)
    return board
#end-def
''' Muestra por consola el tablero de juego actual.
@Entradas -> board(list): tablero de juego
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
                print(Fore.BLACK + green + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "B" or boardTemp[i][j] == "B!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(blue + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "Y" or boardTemp[i][j] == "Y!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(Fore.BLACK + yellow + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "W" or boardTemp[i][j] == "W!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(Fore.BLACK +white + " {:3}".format(boardTemp[i][j]), end = " ")
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
''' Eliminar camino correspondiente a la casilla ingresada si esta se encuentra 'llena'.
@Entradas -> element(string): coordenada correspondiente a la casilla actual.
             board(list): tablero de juego.
@Salida -> retorna 'bool' True cuando se elimina un camino.
'''
def checkE(element, board):
    if len(pathR) > 0:
        if element in pathR:
            for r in range (len(pathR)):
                board[int(pathR[r][0])][int(pathR[r][1])] = '0'
            #end for
            pathR.clear()
            return True
        #end if
    #end if
    if len(pathB) > 0:
        if element in pathB:
            for b in range (len(pathB)):
                board[int(pathB[b][0])][int(pathB[b][1])] = '0'
            #end for
            pathB.clear()
            return True
        #end if
    #end if
    if len(pathY) > 0:
        if element in pathY:
            for y in range (len(pathY)):
                board[int(pathY[y][0])][int(pathY[y][1])] = '0'
            #end for
            pathY.clear()
            return True
        #end if
    #end if
    if len(pathG) > 0:
        if element in pathG:
            for g in range (len(pathG)):
                board[int(pathG[g][0])][int(pathG[g][1])] = '0'
            #end for
            pathG.clear()
            return True
        #end if
    #end if
    if len(pathW) > 0:
        if element in pathW:
            for w in range (len(pathW)):
                board[int(pathW[w][0])][int(pathW[w][1])] = '0'
            #end for
            pathW.clear()
            return True
        #end if
    #end if
    if len(pathC) > 0:
        if element in pathC:
            for c in range (len(pathC)):
                board[int(pathC[c][0])][int(pathC[c][1])] = '0'
            #end for
            pathC.clear()
            return True
        #end if
    #end if
    if len(pathP) > 0:
        if element in pathP:
            for p in range (len(pathP)):
                board[int(pathP[p][0])][int(pathP[p][1])] = '0'
            #end for
            pathP.clear()
            return True
        #end if
    #end if
#end def
''' Obtiene todas las casillas adyacentes que se encuentran del mismo color a la casilla a verificar.
@Entradas -> board(list): tablero actual de juego
             color(string): letra del color correspondiente a la casilla
                            para la cual se quieren hallar los adyacentes.
             i(int): fila de la casilla para la cual
                     se quieren hallar los adyacentes.
             j(int): columna de la casilla para la cual
                     se quieren hallar los adyacentes.
@Salida -> adjacents(list): lista de vectores de long. 2 correspondiente a
                            las coordenadas de las casillas adyacentes que
                            tienen el mismo color.
'''
def getAdj(board, color, i, j):
    n = len(board)
    adjacents = []
    if i > 0:
        if board[i-1][j] == color or board[i-1][j] == color+"!": #Si su casilla de arriba es del mismo color
            adjacents.append([i-1, j])
        #end if
    #end if
    if j > 0:
        if board[i][j-1] == color or board[i][j-1] == color+"!": #Si su casilla izquierda es del mismo color
            adjacents.append([i, j-1])
        #end if
    #end if
    if i < n-1:
        if board[i+1][j] == color or board[i+1][j] == color+"!": #Si su casilla de abajo es del mismo color
            adjacents.append([i+1, j])
        #end if
    #end if
    if j < n-1:
        if board[i][j+1] == color or board[i][j+1] == color+"!": #Si su casilla derecha es del mismo color
            adjacents.append([i, j+1])
        #end if
    #end if
    return adjacents
#end def
''' Verifica si existe otro camino del mismo color de la casilla ingresada.
@Entradas -> color(string): letra del color correspondiente a la casilla actual.
             board(list): tablero actual de juego.
             coordenate(string): coordenada correspondiente a la casilla actual.
@Salida -> retorna 'bool' True cuando ya existe un camino desde algún xInitial.
'''
def verifyPath(color, board, coordenate):
    iC = int(coordenate[0])
    jC = int(coordenate[1])
    adjacentsC = getAdj(board, color, iC, jC)
    if len(adjacentsC) == 1:
        adjC = str(adjacentsC[0][0])+str(adjacentsC[0][1])
        if color == 'R':
            if adjC == rInitial[0]:
                initial1 = [int(rInitial[1][0]),int(rInitial[1][1])]
                for r in range(len(pathR)):
                    i = int(pathR[r][0])
                    j = int(pathR[r][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial1 in adjacents:
                        return True
                    #end if
                #end for
            elif adjC == rInitial[1]:
                initial0 = [int(rInitial[0][0]),int(rInitial[0][1])]
                for r in range(len(pathR)):
                    i = int(pathR[r][0])
                    j = int(pathR[r][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial0 in adjacents:
                        return True
                    #end if
                #end for
            #end if
        #end if
        if color == 'B':
            if adjC == bInitial[0]:
                initial1 = [int(bInitial[1][0]),int(bInitial[1][1])]
                for b in range(len(pathB)):
                    i = int(pathB[b][0])
                    j = int(pathB[b][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial1 in adjacents:
                        return True
                    #end if
                #end for
            elif adjC == bInitial[1]:
                initial0 = [int(bInitial[0][0]),int(bInitial[0][1])]
                for b in range(len(pathB)):
                    i = int(pathB[b][0])
                    j = int(pathB[b][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial0 in adjacents:
                        return True
                    #end if
                #end for
            #end if
        #end if
        if color == 'Y':
            if adjC == yInitial[0]:
                initial1 = [int(yInitial[1][0]),int(yInitial[1][1])]
                for y in range(len(pathY)):
                    i = int(pathY[y][0])
                    j = int(pathY[y][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial1 in adjacents:
                        return True
                    #end if
                #end for
            elif adjC == yInitial[1]:
                initial0 = [int(yInitial[0][0]),int(yInitial[0][1])]
                for y in range(len(pathY)):
                    i = int(pathY[y][0])
                    j = int(pathY[y][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial0 in adjacents:
                        return True
                    #end if
                #end for
            #end if
        #end if
        if color == 'G':
            if adjC == gInitial[0]:
                initial1 = [int(gInitial[1][0]),int(gInitial[1][1])]
                for g in range(len(pathG)):
                    i = int(pathG[g][0])
                    j = int(pathG[g][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial1 in adjacents:
                        return True
                    #end if
                #end for
            elif adjC == gInitial[1]:
                initial0 = [int(gInitial[0][0]),int(gInitial[0][1])]
                for g in range(len(pathG)):
                    i = int(pathG[g][0])
                    j = int(pathG[g][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial0 in adjacents:
                        return True
                    #end if
                #end for
            #end if
        #end if
        if color == 'W':
            if adjC == wInitial[0]:
                initial1 = [int(wInitial[1][0]),int(wInitial[1][1])]
                for w in range(len(pathW)):
                    i = int(pathW[w][0])
                    j = int(pathW[w][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial1 in adjacents:
                        return True
                    #end if
                #end for
            elif adjC == wInitial[1]:
                initial0 = [int(wInitial[0][0]),int(wInitial[0][1])]
                for w in range(len(pathW)):
                    i = int(pathW[w][0])
                    j = int(pathW[w][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial0 in adjacents:
                        return True
                    #end if
                #end for
            #end if
        #end if
        if color == 'C':
            if adjC == cInitial[0]:
                initial1 = [int(cInitial[1][0]),int(cInitial[1][1])]
                for c in range(len(pathC)):
                    i = int(pathC[c][0])
                    j = int(pathC[c][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial1 in adjacents:
                        return True
                    #end if
                #end for
            elif adjC == cInitial[1]:
                initial0 = [int(cInitial[0][0]),int(cInitial[0][1])]
                for c in range(len(pathC)):
                    i = int(pathC[c][0])
                    j = int(pathC[c][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial0 in adjacents:
                        return True
                    #end if
                #end for
            #end if
        #end if
        if color == 'P':
            if adjC == pInitial[0]:
                initial1 = [int(pInitial[1][0]),int(pInitial[1][1])]
                for p in range(len(pathP)):
                    i = int(pathP[p][0])
                    j = int(pathP[p][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial1 in adjacents:
                        return True
                    #end if
                #end for
            elif adjC == pInitial[1]:
                initial0 = [int(pInitial[0][0]),int(pInitial[0][1])]
                for p in range(len(pathP)):
                    i = int(pathP[p][0])
                    j = int(pathP[p][1])
                    adjacents = getAdj(board, color, i, j)
                    if initial0 in adjacents:
                        return True
                    #end if
                #end for
            #end if
        #end if
    #end if
    return False
#end def
''' Agrega casilla ingresada al camino correspondiente (haciendo las verificaciones necesarias).
@Entradas -> color(string): letra del color correspondiente a la casilla actual.
             board(list): tablero actual de juego.
             coordenate(string): coordenada correspondiente a la casilla actual.
@Salida -> actualiza el pathX de la casilla ingresada.
'''
def addPath(color, coordenate, board):
    checkE(coordenate, board)
    if color == 'R':
        if len(pathR) > 0:
            if verifyPath(color, board, coordenate):
                for r in range (len(pathR)):
                    board[int(pathR[r][0])][int(pathR[r][1])] = '0'
                #end for
                pathR.clear()
                pathR.append(coordenate)
            else:
                pathR.append(coordenate)
        else:
            pathR.append(coordenate)
        #end if
    elif color == 'B':
        if len(pathB) > 0:
            if verifyPath(color, board, coordenate):
                for b in range (len(pathB)):
                    board[int(pathB[b][0])][int(pathB[b][1])] = '0'
                #end for
                pathB.clear()
                pathB.append(coordenate)
            else:
                pathB.append(coordenate)
        else:
            pathB.append(coordenate)
        #end if
    elif color == 'Y':
        if len(pathY) > 0:
            if verifyPath(color, board, coordenate):
                for y in range (len(pathY)):
                    board[int(pathY[y][0])][int(pathY[y][1])] = '0'
                #end for
                pathY.clear()
                pathY.append(coordenate)
            else:
                pathY.append(coordenate)
        else:
            pathY.append(coordenate)
        #end if
    elif color == 'G':
        if len(pathG) > 0:
            if verifyPath(color, board, coordenate):
                for g in range (len(pathG)):
                    board[int(pathG[g][0])][int(pathG[g][1])] = '0'
                #end for
                pathG.clear()
                pathG.append(coordenate)
            else:
                pathG.append(coordenate)
        else:
            pathG.append(coordenate)
        #end if
    elif color == 'W':
        if len(pathW) > 0:
            if verifyPath(color, board, coordenate):
                for w in range (len(pathW)):
                    board[int(pathW[w][0])][int(pathW[w][1])] = '0'
                #end for
                pathW.clear()
                pathW.append(coordenate)
            else:
                pathW.append(coordenate)
        else:
            pathW.append(coordenate)
        #end if
    elif color == 'C':
        if len(pathC) > 0:
            if verifyPath(color, board, coordenate):
                for c in range (len(pathC)):
                    board[int(pathC[c][0])][int(pathC[c][1])] = '0'
                #end for
                pathC.clear()
                pathC.append(coordenate)
            else:
                pathC.append(coordenate)
        else:
            pathC.append(coordenate)
        #end if
    elif color == 'P':
        if len(pathP) > 0:
            if verifyPath(color, board, coordenate):
                for p in range (len(pathP)):
                    board[int(pathP[p][0])][int(pathP[p][1])] = '0'
                #end for
                pathP.clear()
                pathP.append(coordenate)
            else:
                pathP.append(coordenate)
        else:
            pathP.append(coordenate)
    #end if
#end def
''' Elimina coordenada del pathX.
@Entradas -> color(string): letra del color correspondiente a la casilla actual.
             element(string): coordenada correspondiente a la casilla actual.
@Salida -> actualiza el pathX (elimina el elemento que se desea remover de la lista).
'''
def removeE(color, element):
    if color == 'R' and element not in rInitial:
        pathR.remove(element)
    elif color == 'G' and element not in gInitial:
        pathG.remove(element)
    elif color == 'Y' and element not in yInitial:
            pathY.remove(element)
    elif color == 'W' and element not in wInitial:
        pathW.remove(element)
    elif color == 'B' and element not in bInitial:
        pathB.remove(element)
    elif color == 'C' and element not in cInitial:
        pathC.remove(element)
    elif color == 'P' and element not in pInitial:
        pathP.remove(element)
    #end if
#end def
''' Respecto a una casilla, elimina todo el camino existente después de la misma
@Entradas -> color(string): letra del color correspondiente a la casilla actual.
             coordenate(string): coordenada correspondiente a la casilla actual.
             board(list): tablero actual de juego.  
@Salida -> actualiza el pathX.
'''
def removeNext(color, coordenate, board):
    if color == 'R':
        indice = False
        while not indice:
            board[int(pathR[-1][0])][int(pathR[-1][1])] = '0'
            removeE(color, pathR[-1])
            if pathR[-1] == coordenate:
                indice = True
            #end if
        #end while
    elif color == 'G':
        indice = False
        while not indice:
            board[int(pathG[-1][0])][int(pathG[-1][1])] = '0'
            removeE(color, pathG[-1])
            if pathG[-1] == coordenate:
                indice = True
            #end if
        #end while
    elif color == 'Y':
        indice = False
        while not indice:
            board[int(pathY[-1][0])][int(pathY[-1][1])] = '0'
            removeE(color, pathY[-1])
            if pathY[-1] == coordenate:
                indice = True
            #end if
        #end while
    elif color == 'W':
        indice = False
        while not indice:
            board[int(pathW[-1][0])][int(pathW[-1][1])] = '0'
            removeE(color, pathW[-1])
            if pathW[-1] == coordenate:
                indice = True
            #end if
        #end while
    elif color == 'B':
        indice = False
        while not indice:
            board[int(pathB[-1][0])][int(pathB[-1][1])] = '0'
            removeE(color, pathB[-1])
            if pathB[-1] == coordenate:
                indice = True
            #end if
        #end while
    elif color == 'C':
        indice = False
        while not indice:
            board[int(pathC[-1][0])][int(pathC[-1][1])] = '0'
            removeE(color, pathC[-1])
            if pathC[-1] == coordenate:
                indice = True
            #end if
        #end while
    elif color == 'P':
        indice = False
        while not indice:
            board[int(pathP[-1][0])][int(pathP[-1][1])] = '0'
            removeE(color, pathP[-1])
            if pathP[-1] == coordenate:
                indice = True
            #end if
        #end while
    #end if
#end def
''' Verifica casillas adyacentes
@Entradas -> board(list): tablero de juego actual.
             coorBox(string): coordenada adyacente a la casilla ingresada.
@Salida -> eliminar casillas adyacentes
'''
def checkAdjacents(board, coordBox):
    i = int(coordBox.split(",")[0])
    j = int(coordBox.split(",")[1])
    color = (board[i][j])
    if color == 'R':
        if len(pathR)>0:
            if pathR[-1] != str(i)+str(j):
                removeNext(color, str(i)+str(j), board)
            #end if
        #end if
    elif color == 'R!':
        if len(pathR)>0:
            for r in pathR:
                board[int(r[0])][int(r[1])] = '0'
            pathR.clear()
        #end if
    elif color == 'B':
        if len(pathB)>0:
            if pathB[-1] != str(i)+str(j):
                removeNext(color, str(i)+str(j), board)
            #end if
        #end if
    elif color == 'B!':
        if len(pathB)>0:
            for b in pathB:
                board[int(b[0])][int(b[1])] = '0'
            pathB.clear()
        #end if
    elif color == 'Y':
        if len(pathY)>0:
            if pathY[-1] != str(i)+str(j):
                removeNext(color, str(i)+str(j), board)
            #end if
        #end if
    elif color == 'Y!':
        if len(pathY)>0:
            for y in pathY:
                board[int(y[0])][int(y[1])] = '0'
            pathY.clear()
        #end if
    elif color == 'W':
        if len(pathW)>0:
            if pathW[-1] != str(i)+str(j):
                removeNext(color, str(i)+str(j), board)
            #end if
        #end if
    elif color == 'W!':
        if len(pathW)>0:
            for w in pathW:
                board[int(w[0])][int(w[1])] = '0'
            pathW.clear()
        #end if
    elif color == 'G':
        if len(pathG)>0:
            if pathG[-1] != str(i)+str(j):
                removeNext(color, str(i)+str(j), board)
            #end if
        #end if
    elif color == 'G!':
        if len(pathG)>0:
            for g in pathG:
                board[int(g[0])][int(g[1])] = '0'
            pathG.clear()
        #end if
    elif color == 'C':
        if len(pathC)>0:
            if pathC[-1] != str(i)+str(j):
                removeNext(color, str(i)+str(j), board)
            #end if
        #end if
    elif color == 'C!':
        if len(pathC)>0:
            for c in pathC:
                board[int(c[0])][int(c[1])] = '0'
            pathC.clear()
        #end if
    elif color == 'P':
        if len(pathP)>0:
            if pathP[-1] != str(i)+str(j):
                removeNext(color, str(i)+str(j), board)
            #end if
        #end if
    elif color == 'P!':
        if len(pathP)>0:
            for p in pathP:
                board[int(p[0])][int(p[1])] = '0'
            pathP.clear()
        #end if
    #end if        
#end def
''' Obtener la posición en el pathX de una casilla.
@Entradas -> color(string): letra del color correspondiente a la casilla actual.
             i(int): fila de la casilla para la cual
                     se quiere encontrar la posición.
             j(int): columna de la casilla para la cual
                     se quiere encontrar la posición.
@Salidas -> retorna un entero:
                -1:  si la casilla no se encuentra en el path.
                int: número correspondiente al índice en el que se encuentra la casilla.
'''
def getIndex(color, i, j):
    if color == 'R':
        return pathR.index(str(i) + str(j)) if (str(i) + str(j)) in pathR else -1
    elif color == 'B':
        return pathB.index(str(i) + str(j)) if (str(i) + str(j)) in pathB else -1
    elif color == 'Y':
        return pathY.index(str(i) + str(j)) if (str(i) + str(j)) in pathY else -1
    elif color == 'G':
        return pathG.index(str(i) + str(j)) if (str(i) + str(j)) in pathG else -1
    elif color == 'W':
        return pathW.index(str(i) + str(j)) if (str(i) + str(j)) in pathW else -1
    elif color == 'C':
        return pathC.index(str(i) + str(j)) if (str(i) + str(j)) in pathC else -1
    elif color == 'P':
        return pathP.index(str(i) + str(j)) if (str(i) + str(j)) in pathP else -1
    #end if
#end def
''' Obtener una coordenada a partir de una posición específica.
@Entradas -> color(string): letra del color correspondiente al path en el que se desea buscar.
             pos(int): posición (ínidice) de la cual 
                       se quiere obtener la coordenada.
@Salidas -> retorna un string con la coordenada encontrada.
'''
def getPosPath(color, pos):
    if color == 'R':
        return pathR[pos]
    elif color == 'B':
        return pathB[pos]
    elif color == 'Y':
        return pathY[pos]
    elif color == 'G':
        return pathG[pos]
    elif color == 'W':
        return pathW[pos]
    elif color == 'C':
        return pathC[pos]
    elif color == 'P':
        return pathP[pos]
    #end if
#end def
''' Verificar si la casilla ingresada se puede agregar y retornar la casilla que permite llegar a la misma.
@Entradas -> board(list): tablero actual de juego.
             color(string): letra del color correspondiente a la casilla actual.
             coordenate(string): coordenada correspondiente a la casilla actual.
@Salida -> retorna una lista que contiene:
            lista[0](string): coordenada que permite llegar a la casilla actual.
            lista[1](bool): valida que exista una casilla adyacente que permita
                            llegar a la casilla actual.
'''
def checkBox(board, color, coordenate):
    i = int(coordenate[0])
    j = int(coordenate[1])
    n = len(board)
    extremo = ""
    up, down, left, right = -1, -1, -1, -1
    if board[i][j] == color:
        print(Fore.RED + "******La casilla ya tiene el color seleccionado.\n")
        removeNext(color, coordenate, board)
        return ['E', False]
    elif board[i][j] == "0" or "!" not in board[i][j]:
        if i > 0:
            if board[i-1][j] == color: #Si su casilla de arriba es del mismo color
                up = getIndex(color, i-1, j)
            elif board[i-1][j] == color+"!":
                extremo = str(i-1) + "," + str(j) 
            #end if    
        #end if
        if j > 0:
            if board[i][j-1] == color : #Si su casilla izquierda es del mismo color
                left = getIndex(color, i, j-1)
            elif board[i][j-1] == color+"!":
                extremo = str(i) + "," + str(j-1)
            #end if
        #end if
        if i < n-1:
            if board[i+1][j] == color: #Si su casilla de abajo es del mismo color
                down = getIndex(color, i+1, j)
            elif board[i+1][j] == color+"!":
                extremo = str(i+1) + "," + str(j)
            #end if
        #end if
        if j < n-1:
            if board[i][j+1] == color: #Si su casilla derecha es del mismo color
                right = getIndex(color, i, j+1)
            elif board[i][j+1] == color+"!":
                extremo = str(i) + "," + str(j+1)
            #end if
        #end if
        if up != -1 or down != -1 or left != -1 or right != -1:
            posLastAdj = max([up, down, left, right]) #Posición del último adyacente en path
            lastAdj = getPosPath(color, posLastAdj)
            return [lastAdj[0] + "," + lastAdj[1], True]
        #end if
        if extremo != "":
            return [extremo, True]
        #end if
        print(Fore.RED + "******No hay casillas adyacentes del color seleccionado.\n")
    #end if
    if "!" in board[i][j]:
        print(Fore.RED + "******No puede cambiar una casilla inicial.\n")
    #end if
    return ['F', False]
#end def
''' Inicar si el tablero ya fue llenado en su totalidad.
@Entradas -> board(list): tablero actual de juego.
@Salida -> retorna 'bool' que indica si ya está completamente lleno.
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
''' Verificar si cada valor inicial (extremo) de un color tiene una casilla adyacente perteneciente al pathX.
@Entradas -> initial(list): lista de strings correspondientes a los extremos de un color. 
             path(list): lista de strings correspondientes al camino de un color.
             dim: dimensiones del tablero de juego
@Salida -> retorna 'bool' cuando el camino está completo
'''
def checkPath(initial, path, dim):
    win1 = False
    win2 = False
    if (int(initial[0][0]) > 0) or (int(initial[1][0]) > 0): #Casilla Arriba
        new = str(int(initial[0][0])-1) + initial[0][1]
        if new in path:
            win1 = True
        new = str(int(initial[1][0])-1) + initial[1][1]
        if new in path:
            win2 = True
    #end if
    if (int(initial[0][0]) < dim-1) or (int(initial[1][0]) < dim-1): #Casilla Abajo
        new = str(int(initial[0][0])+1) + initial[0][1]
        if new in path:
            win1 = True
        new = str(int(initial[1][0])+1) + initial[1][1]
        if new in path:
            win2 = True
    #end if
    if (int(initial[0][1]) > 0) or (int(initial[1][1]) > 0): #Casilla Izquierda
        new = initial[0][0] + str(int(initial[0][1])-1)
        if new in path:
            win1 = True
        new = initial[1][0] + str(int(initial[1][1])-1)
        if new in path:
            win2 = True
    #end if
    if (int(initial[0][1]) < dim-1) or (int(initial[1][1]) < dim-1): #Casilla Derecha
        new = initial[0][0] + str(int(initial[0][1])+1)
        if new in path:
            win1 = True
        new = initial[1][0] + str(int(initial[1][1])+1)
        if new in path:
            win2 = True
    #end if
    if win1 and win2:
        return True
    #end if
#end def
''' Verificar si el tablero está correctamente lleno
@Entradas -> board(list): tablero actual de juego.
@Salida -> retorna un dato 'bool' que indica si ya el jugador completó el nivel.
'''
def checkWinner(board):
    dim = len(board)
    if (len(pathR)) > 0 and len(rInitial) > 0:
        winR = checkPath(rInitial, pathR, dim)
    else:
        if len(rInitial) > 0:
            winR = False
        else:
            winR = True
    if (len(pathB)) > 0 and len(bInitial) > 0:
        winB = checkPath(bInitial, pathB, dim)
    else:
        if len(bInitial) > 0:
            winB = False
        else:
            winB = True
    if (len(pathY)) > 0 and len(yInitial) > 0:
        winY = checkPath(yInitial, pathY, dim)
    else:
        if len(yInitial) > 0:
            winY = False
        else:
            winY = True
    if (len(pathG)) > 0 and len(gInitial) > 0:
        winG = checkPath(gInitial, pathG, dim)
    else:
        if len(gInitial) > 0:
            winG = False
        else:
            winG = True
    if (len(pathW)) > 0 and len(wInitial) > 0:
        winW = checkPath(wInitial, pathW, dim)
    else:
        if len(wInitial) > 0:
            winW = False
        else:
            winW = True
    if (len(pathC)) > 0 and len(cInitial) > 0:
        winC = checkPath(cInitial, pathC, dim)
    else:
        if len(cInitial) > 0:
            winC = False
        else:
            winC = True
    if (len(pathP)) > 0 and len(pInitial) > 0:
        winP = checkPath(pInitial, pathP, dim)
    else:
        if len(pInitial) > 0:
            winP = False
        else:
            winP = True
    if winR and winB and winY and winG and winW and winC and winP:
        return True
    return False
#end def
''' Eliminar todos los datos almacenados en xInitial y en pathX.'''
def resetGame():
    rInitial.clear()
    bInitial.clear()
    yInitial.clear()
    gInitial.clear()
    wInitial.clear()
    cInitial.clear()
    pInitial.clear()
    pathR.clear()
    pathB.clear()
    pathG.clear()
    pathY.clear()
    pathW.clear()
    pathC.clear()
    pathP.clear()
''' Controlar los movimientos del juego.
@Entradas -> board(list): tablero actual de juego.
'''
def selectMove(board):
    finished = False #Verificar que el juego no haya finalizado (cuando todas las casillas tienen color)
    win = False
    out = False
    while not finished and not out:
        parameters = False #Verificar que los parámetros estén correctos y que haya seleccionado una casilla correcta
        while not parameters:
            print("Recuerde que los colores son:  ", red + " {:4}".format("Red"), Fore.BLACK + green + " {:6}".format("Green"), blue + " {:5}".format("Blue"), Fore.BLACK + yellow + " {:7}".format("Yellow"), Fore.BLACK + white + " {:6}".format("White"), cyan + " {:5}".format("Cyan"), purple + " {:7}".format("Purple"), end = " ")
            print("\n")
            print("(Si desea salir del juego ingrese la letra X)")
            move = str(input("Digite la inicial del color que desea utilizar y la casilla que desea jugar (Ej: R 34): "))
            if move.upper() != "X":
                movements = move.split()
                if len(movements) == 2:
                    if movements[0].isalpha():
                        if movements[1].isnumeric():
                            if movements[0].upper() == "R" or movements[0].upper() == "G" or movements[0].upper() == "B" or movements[0].upper() == "Y" or movements[0].upper() == "W" or movements[0].upper() == "C" or movements[0].upper() == "P":
                                if len(movements[1])  == 2:
                                    if (int(movements[1][0]) >= 0) and (int(movements[1][0]) < len(board)) and (int(movements[1][1]) >= 0) and (int(movements[1][1]) < len(board)):
                                        boxChecked = checkBox(board, movements[0].upper(), movements[1])                                        
                                        if boxChecked[0] != 'F' and boxChecked[0] != 'E':
                                            checkAdjacents(board, boxChecked[0])
                                            addPath(movements[0].upper(), movements[1], board)
                                        if boxChecked[0] == 'E':
                                            showBoard(board)
                                        parameters = boxChecked[1]
                                    else:
                                        print(Fore.RED + "******Número de casilla incorrecta.\n")
                                    #end if
                                else:
                                    print(Fore.RED + "******Número de casilla incorrecta.\n")
                                #end if
                            else:
                                print(Fore.RED + "******Inicial de color inválida.\n")
                            #end if
                        else:
                            print (Fore.RED + "******Parámetro casilla incorrecto.\n")
                        #end if
                    else:
                        print (Fore.RED + "******Parámetro color incorrecto.\n")
                    #end if
                else:
                    print(Fore.RED + "******Cantidad de parámetros enviados incorrecta.\n")
                #end if
            else:
                out = True
                parameters = True
                resetGame()
            #end if
        #end while
        if not out:
            board[int(movements[1][0])][int(movements[1][1])] = movements[0].upper()
            showBoard(board)
            finished = checkFinished(board)
            if finished:
                win = checkWinner(board)
                if win == False:
                    finished = False
                    print(Fore.RED + "\t\tNo ha completado de manera correcta el nivel :(")
                    print(Fore.GREEN + "\t\t\t\nPor favor, siga intentando :D")
                else:
                    finished = True
                    resetGame()
                    print("\t\tHa superado el nivel con éxito! ")
                #end if
            #end if
        #end if
    #end while
#end def