"""
    Autores: 
        María Camila Aguirre Collante
        Jessica Tatiana Naizaque Guevara
"""

import queue, time, copy
from Interface import *

''' Se aplica el algoritmo de aproximación A*
    cost = g + h
        ° g : costo de llegar a la celda (coordenada) en la que se encuentra.
        ° h : costo calculado mediante la distancia de Manhattan entre la 
              coordenada actual y la coordenada final.
'''
rInitialInt = []
bInitialInt = []
yInitialInt = []
gInitialInt = []
wInitialInt = []
cInitialInt = []
pInitialInt = []

#'Historiales' de los caminos por color
rRecord = []
bRecord = []
yRecord = []
gRecord = []
wRecord = []
cRecord = []
pRecord = []

''' Lista de coordenadas iniciales como enteros
'''
def coordenatesInt():
    if len(rInitial) > 0:
        begin = []
        end = []
        begin.append(int(rInitial[0][0]))
        begin.append(int(rInitial[0][1]))
        end.append(int(rInitial[1][0]))
        end.append(int(rInitial[1][1]))
        rInitialInt.append(begin) 
        rInitialInt.append(end)
    #end if
    if len(bInitial) > 0:
        begin = []
        end = []
        begin.append(int(bInitial[0][0]))
        begin.append(int(bInitial[0][1]))
        end.append(int(bInitial[1][0]))
        end.append(int(bInitial[1][1]))
        bInitialInt.append(begin) 
        bInitialInt.append(end)
    #end if
    if len(yInitial) > 0:
        begin = []
        end = []
        begin.append(int(yInitial[0][0]))
        begin.append(int(yInitial[0][1]))
        end.append(int(yInitial[1][0]))
        end.append(int(yInitial[1][1]))
        yInitialInt.append(begin) 
        yInitialInt.append(end)
    #end if
    if len(gInitial) > 0:
        begin = []
        end = []
        begin.append(int(gInitial[0][0]))
        begin.append(int(gInitial[0][1]))
        end.append(int(gInitial[1][0]))
        end.append(int(gInitial[1][1]))
        gInitialInt.append(begin) 
        gInitialInt.append(end)
    #end if
    if len(wInitial) > 0:
        begin = []
        end = []
        begin.append(int(wInitial[0][0]))
        begin.append(int(wInitial[0][1]))
        end.append(int(wInitial[1][0]))
        end.append(int(wInitial[1][1]))
        wInitialInt.append(begin) 
        wInitialInt.append(end)
    #end if
    if len(cInitial) > 0:
        begin = []
        end = []
        begin.append(int(cInitial[0][0]))
        begin.append(int(cInitial[0][1]))
        end.append(int(cInitial[1][0]))
        end.append(int(cInitial[1][1]))
        cInitialInt.append(begin) 
        cInitialInt.append(end)
    #end if
    if len(pInitial) > 0:
        begin = []
        end = []
        begin.append(int(pInitial[0][0]))
        begin.append(int(pInitial[0][1]))
        end.append(int(pInitial[1][0]))
        end.append(int(pInitial[1][1]))
        pInitialInt.append(begin) 
        pInitialInt.append(end)
    #end if
#end def

''' Distancia de Manhattan entre puntos iniciales de cada color
@Salidas -> lista de 'tuplas' ordenadas según la distancia 
'''
def getPriorityColors():
    distances = []
    if len(rInitialInt) > 0:
        distanceR = abs(rInitialInt[0][0] - rInitialInt[1][0]) + abs(rInitialInt[0][1] - rInitialInt[1][1])
        distances.append(('R', distanceR))
    #end if
    if len(bInitialInt) > 0:
        distanceB = abs(bInitialInt[0][0] - bInitialInt[1][0]) + abs(bInitialInt[0][1] - bInitialInt[1][1])
        distances.append(('B', distanceB))
    #end if
    if len(yInitialInt) > 0:
        distanceY = abs(yInitialInt[0][0] - yInitialInt[1][0]) + abs(yInitialInt[0][1] - yInitialInt[1][1])
        distances.append(('Y', distanceY))
    #end if
    if len(gInitialInt) > 0:
        distanceG = abs(gInitialInt[0][0] - gInitialInt[1][0]) + abs(gInitialInt[0][1] - gInitialInt[1][1])
        distances.append(('G', distanceG))
    #end if
    if len(wInitialInt) > 0:
        distanceW = abs(wInitialInt[0][0] - wInitialInt[1][0]) + abs(wInitialInt[0][1] - wInitialInt[1][1])
        distances.append(('W', distanceW))
    #end if
    if len(cInitialInt) > 0:
        distanceC = abs(cInitialInt[0][0] - cInitialInt[1][0]) + abs(cInitialInt[0][1] - cInitialInt[1][1])
        distances.append(('C', distanceC))
    #end if
    if len(pInitialInt) > 0:
        distanceP = abs(pInitialInt[0][0] - pInitialInt[1][0]) + abs(pInitialInt[0][1] - pInitialInt[1][1])
        distances.append(('P', distanceP))
    #end if
    return sorted(distances, key=lambda t: t[1])
#end def

''' Casillas adyacentes 'libres' a las que se puede mover
@Salidas -> adjacentes(list): coordenadas adyacentes disponibles a la casilla ingresada
'''
def availableAdj(board, color, row, col):
    n = len(board)
    adjacents = []
    if row > 0:
        if board[row-1][col] == '0': #Si su casilla de arriba es igual a 0
            adjacents.append([row-1, col])
    #end if
    if col > 0:
        if board[row][col-1] == '0': #Si su casilla izquierda es igual a 0
            adjacents.append([row, col-1])
    #end if
    if row < n-1:
        if board[row+1][col] == '0': #Si su casilla de abajo es igual a 0
            adjacents.append([row+1, col])
    #end if
    if col < n-1:
        if board[row][col+1] == '0': #Si su casilla derecha es igual a 0
            adjacents.append([row, col+1])
    #end if
    return adjacents
#end def

''' Casillas adyacentes no iniciales a las que se puede mover
@Salidas -> adjacentes(list): coordenadas adyacentes disponibles a la casilla ingresada
'''
def availableAdjComplete(board, color, row, col):
    n = len(board)
    adjacents = []
    if row > 0:
        if board[row-1][col] == '0': #Si su casilla de arriba es igual a 0
            adjacents.append([row-1, col])
        elif '!' not in board[row-1][col]: #Si su casilla de arriba no es un punto inicial
            adjacents.append([row-1, col])
            #end if
        #end if
    #end if
    if col > 0:
        if board[row][col-1] == '0': #Si su casilla izquierda es igual a 0
            adjacents.append([row, col-1])
        elif '!' not in board[row][col-1]: #Si su casilla izquierda no es un punto inicial
            adjacents.append([row, col-1])
            #end if
        #end if
    #end if
    if row < n-1:
        if board[row+1][col] == '0': #Si su casilla de abajo es igual a 0
            adjacents.append([row+1, col])
        elif '!' not in board[row+1][col]: #Si su casilla de abajo no es un punto inicial
            adjacents.append([row+1, col])
            #end if
        #end if
    #end if
    if col < n-1:
        if board[row][col+1] == '0': #Si su casilla derecha es igual a 0
            adjacents.append([row, col+1])
        elif '!' not in board[row][col+1]: #Si su casilla derecha no es un punto inicial
            adjacents.append([row, col+1])
            #end if
        #end if
    #end if
    return adjacents
#end def

''' Calcular costo de coordenada actual
'''
def cost(board, color, row, col, startCoord):
    if board[row][col] != '0':
        g = 10
    else:
        g = 1
    if color == 'R':
        if len(pathR) > 0:
            if board[row][col] != '0':
                g = len(pathR) + 10
            else:
                g = len(pathR) + 1
            #end if
        #end if
        copyPath = pathR.copy()
        copyPath.append(str(row) + str(col))
        inRecord = False
        for record in rRecord:
            if (all(x in record for x in copyPath)):
                inRecord = True                    
            #end if
        #
        if inRecord:
            g += 7
        if startCoord == 'begin':
            h = abs(row - rInitialInt[1][0]) + abs(col - rInitialInt[1][1])
        else:
            h = abs(row - rInitialInt[0][0]) + abs(col - rInitialInt[0][1])
    elif color == 'B':
        print('PATH EN COST ', pathB)
        if len(pathB) > 0:
            print('Entra con ', row, ' ', col)
            if board[row][col] != '0':
                g = len(pathB) + 10
            else:
                g = len(pathB) + 1
        #end if
        copyPath = pathB.copy()
        copyPath.append(str(row) + str(col))
        inRecord = False
        #print('\t\t\t\t\t\t\t\t\tRecord cost ', bRecord)
        for record in bRecord:
            if (all(x in record for x in copyPath)):
                #print ('NO ENTRA')
                inRecord = True                    
            #end if
        #
        if inRecord:
            g += 7
        if startCoord == 'begin':
            h = abs(row - bInitialInt[1][0]) + abs(col - bInitialInt[1][1])
        else:
            h = abs(row - bInitialInt[0][0]) + abs(col - bInitialInt[0][1])
    elif color == 'Y':
        if len(pathY) > 0:
            if board[row][col] != '0':
                g = len(pathY) + 10
            else:
                g = len(pathY) + 1
        #end if
        copyPath = pathY.copy()
        copyPath.append(str(row) + str(col))
        inRecord = False
        for record in yRecord:
            if (all(x in record for x in copyPath)):
                inRecord = True                    
            #end if
        #
        if inRecord:
            g += 7
        if startCoord == 'begin':
            h = abs(row - yInitialInt[1][0]) + abs(col - yInitialInt[1][1])
        else: 
            h = abs(row - yInitialInt[0][0]) + abs(col - yInitialInt[0][1])
    elif color == 'G':
        if len(pathG) > 0:
            if board[row][col] != '0':
                g = len(pathG) + 10
            else:
                g = len(pathG) + 1
        #end if
        copyPath = pathG.copy()
        copyPath.append(str(row) + str(col))
        inRecord = False
        for record in gRecord:
            if (all(x in record for x in copyPath)):
                inRecord = True                    
            #end if
        #
        if inRecord:
            g += 7
        if startCoord == 'begin':
            h = abs(row - gInitialInt[1][0]) + abs(col - gInitialInt[1][1])
        else:
            h = abs(row - gInitialInt[0][0]) + abs(col - gInitialInt[0][1])
    elif color == 'W':
        if len(pathW) > 0:
            if board[row][col] != '0':
                g = len(pathW) + 10
            else:
                g = len(pathW) + 1
        #end if
        copyPath = pathW.copy()
        copyPath.append(str(row) + str(col))
        inRecord = False
        for record in wRecord:
            if (all(x in record for x in copyPath)):
                inRecord = True                    
            #end if
        #
        if inRecord:
            g += 7
        if startCoord == 'begin':
            h = abs(row - wInitialInt[1][0]) + abs(col - wInitialInt[1][1])
        else:
            h = abs(row - wInitialInt[0][0]) + abs(col - wInitialInt[0][1])
            print('H: ', h, ' con ', row, ' ', col)
    elif color == 'C':
        if len(pathC) > 0:
            if board[row][col] != '0':
                g = len(pathC) + 10
            else:
                g = len(pathC) + 1
        #end if
        copyPath = pathC.copy()
        copyPath.append(str(row) + str(col))
        inRecord = False
        for record in cRecord:
            if (all(x in record for x in copyPath)):
                inRecord = True                    
            #end if
        #
        if inRecord:
            g += 7
        if startCoord == 'begin':
            h = abs(row - cInitialInt[1][0]) + abs(col - cInitialInt[1][1])
        else:
            h = abs(row - cInitialInt[0][0]) + abs(col - cInitialInt[0][1])
    elif color == 'P':
        if len(pathP) > 0:
            if board[row][col] != '0':
                g = len(pathP) + 10
            else:
                g = len(pathP) + 1
        #end if
        copyPath = pathP.copy()
        copyPath.append(str(row) + str(col))
        inRecord = False
        for record in pRecord:
            if (all(x in record for x in copyPath)):
                inRecord = True                    
            #end if
        #
        if inRecord:
            g += 7
        if startCoord == 'begin':
            h = abs(row - pInitialInt[1][0]) + abs(col - pInitialInt[1][1])
        else:
            h = abs(row - cInitialInt[0][0]) + abs(col - cInitialInt[0][1])
    #end if
    return h + g
#end def    

''' 
'''
def resetActual():
    rInitialInt.clear()
    bInitialInt.clear()
    yInitialInt.clear()
    gInitialInt.clear()
    wInitialInt.clear()
    cInitialInt.clear()
    pInitialInt.clear()
    rRecord.clear()
    bRecord.clear()
    yRecord.clear()
    gRecord.clear()
    wRecord.clear()
    cRecord.clear()
    pRecord.clear()

''' A*: 
    El orden de los colores que serán revisados está dado mediante la distancia 
        de Manhattan entre los puntos iniciales de cada color.

        ° visited(list): 'Nodos' (coordenadas) visitadas
'''
def bestPath(board):
    #Llenar listas 'int' de coordenadas de los puntos iniciales
    coordenatesInt()
    #Obtener lista de 'tuplas' ordenada (revisar colores)
    colors = getPriorityColors()
    countColor = 0
    dim = len(board)
    priorityQueue = queue.PriorityQueue(4) #cola de prioridad
    while not checkWinner(board):# or not checkFinished(board): #Mientras no se haya solucionado el tablero
        if countColor == len(colors): #está "fuera de rango"
            countColor = 0
        #end if
        currentColor = colors[countColor][0]
        #print('Color act: ', currentColor, ' con count ', countColor)
        if currentColor == 'R':
            #print('Entra al color ', pathR)
            #time.sleep(2)
            visited = []#'Nodos' visitados en el path
            startCoord = 'begin'
            completePath = checkPath(rInitial, pathR, dim)
            while not completePath:
                if len(pathR) == 0 and startCoord == 'begin':
                    beginRow, beginCol = rInitialInt[0][0], rInitialInt[0][1] #Coordenada del punto inicial
                    elementsAdd = availableAdj(board, currentColor, beginRow, beginCol)
                    #print('Adyacentes: ', elementsAdd)
                elif len(pathR) == 0 and startCoord == 'end':
                    endRow, endCol = rInitialInt[1][0], rInitialInt[1][1] #Coordenada del punto inicial
                    elementsAdd = availableAdjComplete(board, currentColor, endRow, endCol)
                else: 
                    currentCoor = pathR[-1] #Obtener coordenada de la última casilla
                    currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                    if startCoord == 'begin':
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    else:
                        elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 1 and (board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor or board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor+'!'):
                        if pathR not in rRecord:
                            copyPath = pathR.copy()
                            rRecord.append(copyPath)
                        ind = -1
                        for i in range(len(pathR)-1, -1, -1):
                            if len(availableAdj(board, currentColor, int(pathR[i][0]), int(pathR[i][1]))) != 0:
                                ind = i 
                                i = -1
                        if ind != -1:
                            visited.append([int(pathR[ind+1][0]), int(pathR[ind+1][1])])
                            removeNext(currentColor, pathR[ind], board)
                        if len(pathR) == 0:
                            currentCoor = rInitial[0]
                        else:
                            currentCoor = pathR[-1]
                        currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 0:
                        if not checkPath(rInitial, pathR, dim):
                            lastCoor = currentCoor
                            pathR.remove(currentCoor)
                            board[currentRow][currentCol] = '0'
                            if len(pathR) == 0:
                                currentCoor = rInitial[0]
                            else:
                                currentCoor = pathR[-1]
                            currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                            if startCoord == 'begin':
                                elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                            else:
                                elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                            if [int(lastCoor[0]), int(lastCoor[1])] in elementsAdd:
                                elementsAdd.remove([int(lastCoor[0]), int(lastCoor[1])])
                            #end if
                            for v in visited:
                                if v in elementsAdd:
                                    elementsAdd.remove(v) 
                #end if
                if len(elementsAdd) > 0:
                    for adj in elementsAdd:
                        if len(visited) == 0:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            #print('Costo', currentCost, ' en ', adj)
                            priorityQueue.put((currentCost, adj))
                        elif adj not in visited:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            priorityQueue.put((currentCost, adj))
                    #end for
                    if not priorityQueue.empty():
                        element = priorityQueue.get()
                        visited.append(element[1])
                        coordenate = str(element[1][0])+str(element[1][1])
                        checkE(coordenate, board)
                        board[element[1][0]][element[1][1]] = 'R'
                        pathR.append(coordenate)
                        showBoard(board)
                        #time.sleep(1)
                        #Vacíar cola de prioridad
                        priorityQueue.queue.clear()
                else:
                    startCoord = 'end'
                    if len(pathR) > 0:
                        checkE(pathR[0], board)
                    #end if
                    visited.clear()
                if checkPath(rInitial, pathR, dim):
                    if pathR not in rRecord:
                        copyPath = pathR.copy()
                        rRecord.append(copyPath)
                    completePath = True
                #end if
            #end while
            if checkPath(rInitial, pathR, dim):
                countColor += 1
        #end if
        if currentColor == 'B':
            visited = []#'Nodos' visitados en el path
            startCoord = 'begin'
            completePath = checkPath(bInitial, pathB, dim)
            while not completePath:
                if len(pathB) == 0 and startCoord == 'begin':
                    beginRow, beginCol = bInitialInt[0][0], bInitialInt[0][1] #Coordenada del punto inicial
                    elementsAdd = availableAdj(board, currentColor, beginRow, beginCol)
                elif len(pathB) == 0 and startCoord == 'end':
                    endRow, endCol = bInitialInt[1][0], bInitialInt[1][1] #Coordenada del punto inicial
                    elementsAdd = availableAdjComplete(board, currentColor, endRow, endCol)
                else: 
                    currentCoor = pathB[-1] #Obtener coordenada de la última casilla
                    currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                    if startCoord == 'begin':
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    else:
                        elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                    #print('Adyacentes ', elementsAdd)
                    if len(elementsAdd) == 1 and (board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor or board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor+'!'):
                        if pathB not in bRecord:
                            copyPath = pathB.copy()
                            bRecord.append(copyPath)
                        ind = -1
                        for i in range(len(pathB)-1, -1, -1):
                            if len(availableAdj(board, currentColor, int(pathB[i][0]), int(pathB[i][1]))) != 0:
                                ind = i 
                                i = -1
                        if ind != -1:
                            visited.append([int(pathB[ind+1][0]), int(pathB[ind+1][1])])
                            removeNext(currentColor, pathB[ind], board)
                        if len(pathB) == 0:
                            currentCoor = bInitial[0]
                        else:
                            currentCoor = pathB[-1]
                        currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 0:
                        if not checkPath(bInitial, pathB, dim):
                            lastCoor = currentCoor
                            pathB.remove(currentCoor)
                            board[currentRow][currentCol] = '0'
                            if len(pathB) == 0:
                                currentCoor = bInitial[0]
                            else:
                                currentCoor = pathB[-1]
                            currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                            if startCoord == 'begin':
                                elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                            else:
                                elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                            if [int(lastCoor[0]), int(lastCoor[1])] in elementsAdd:
                                elementsAdd.remove([int(lastCoor[0]), int(lastCoor[1])])
                            #end if
                            for v in visited:
                                if v in elementsAdd:
                                    elementsAdd.remove(v) 
                #end if
                if len(elementsAdd) > 0:
                    for adj in elementsAdd:
                        if len(visited) == 0:
                            #print('ANTES DE COST El record es: ', bRecord)
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            #print('Costo actual ', currentCost, ' de ', adj)
                            priorityQueue.put((currentCost, adj))
                        elif adj not in visited:
                            #print('ANTES DE COST El record es: ', bRecord)
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            #print('Costo actual ', currentCost, ' de ', adj)
                            priorityQueue.put((currentCost, adj))
                    #end for
                    if not priorityQueue.empty():
                        element = priorityQueue.get()
                        #print('Elemento ', element)
                        visited.append(element[1])
                        coordenate = str(element[1][0])+str(element[1][1])
                        checkE(coordenate, board)
                        board[element[1][0]][element[1][1]] = 'B'
                        pathB.append(coordenate)
                        showBoard(board)
                        #time.sleep(1)
                        #Vacíar cola de prioridad
                        priorityQueue.queue.clear()
                else:
                    startCoord = 'end'
                    if len(pathB) > 0:
                        checkE(pathB[0], board)
                    #end if
                    visited.clear()
                if checkPath(bInitial, pathB, dim):
                    #print('Entra al if ini')
                    if pathB not in bRecord:
                        copyPath = pathB.copy()
                        bRecord.append(copyPath)
                        #print('El record es: ', bRecord)
                    completePath = True
                #end if
            #end while 
            if checkPath(bInitial, pathB, dim):
                countColor += 1
        #end if
        if currentColor == 'Y':
            visited = []#'Nodos' visitados en el path
            startCoord = 'begin'
            completePath = checkPath(yInitial, pathY, dim)
            #print('Path: ', pathY, ' and ', completePath)
            while not completePath:
                if len(pathY) == 0 and startCoord == 'begin':
                    beginRow, beginCol = yInitialInt[0][0], yInitialInt[0][1] #Coordenada del punto inicial
                    elementsAdd = availableAdj(board, currentColor, beginRow, beginCol)
                elif len(pathY) == 0 and startCoord == 'end':
                    endRow, endCol = yInitialInt[1][0], yInitialInt[1][1] #Coordenada del punto inicial
                    elementsAdd = availableAdjComplete(board, currentColor, endRow, endCol)
                else: 
                    currentCoor = pathY[-1] #Obtener coordenada de la última casilla
                    currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                    if startCoord == 'begin':
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    else:
                        elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 1 and (board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor or board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor+'!'):
                        if pathY not in yRecord:
                            copyPath = pathY.copy()
                            yRecord.append(copyPath)
                        ind = -1
                        for i in range(len(pathY)-1, -1, -1):
                            if len(availableAdj(board, currentColor, int(pathY[i][0]), int(pathY[i][1]))) != 0:
                                ind = i 
                                i = -1
                        if ind != -1:
                            visited.append([int(pathY[ind+1][0]), int(pathY[ind+1][1])])
                            removeNext(currentColor, pathY[ind], board)
                        if len(pathY) == 0:
                            currentCoor = yInitial[0]
                        else:
                            currentCoor = pathY[-1]
                        currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 0:
                        if not checkPath(yInitial, pathY, dim):
                            lastCoor = currentCoor
                            pathY.remove(currentCoor)
                            board[currentRow][currentCol] = '0'
                            if len(pathY) == 0:
                                currentCoor = yInitial[0]
                            else:
                                currentCoor = pathY[-1]
                            currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                            if startCoord == 'begin':
                                elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                            else:
                                elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                            if [int(lastCoor[0]), int(lastCoor[1])] in elementsAdd:
                                elementsAdd.remove([int(lastCoor[0]), int(lastCoor[1])])
                            #end if
                            for v in visited:
                                if v in elementsAdd:
                                    elementsAdd.remove(v) 
                #end if
                if len(elementsAdd) > 0:
                    for adj in elementsAdd:
                        if len(visited) == 0:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            priorityQueue.put((currentCost, adj))
                        elif adj not in visited:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            priorityQueue.put((currentCost, adj))
                    #end for
                    if not priorityQueue.empty():
                        element = priorityQueue.get()
                        visited.append(element[1])
                        coordenate = str(element[1][0])+str(element[1][1])
                        checkE(coordenate, board)
                        board[element[1][0]][element[1][1]] = 'Y'
                        pathY.append(coordenate)
                        showBoard(board)
                        #time.sleep(1)
                        #Vacíar cola de prioridad
                        priorityQueue.queue.clear()
                else:
                    startCoord = 'end'
                    if len(pathY) > 0:
                        checkE(pathY[0], board)
                    #end if
                    visited.clear()
                if checkPath(yInitial, pathY, dim):
                    if pathY not in yRecord:
                        copyPath = pathY.copy()
                        yRecord.append(copyPath)
                    completePath = True
                #end if
            #end while 
            if checkPath(yInitial, pathY, dim):
                countColor += 1
        #end if
        if currentColor == 'G':
            #print('Entra al color ', pathR)
            visited = []#'Nodos' visitados en el path
            startCoord = 'begin'
            completePath = checkPath(gInitial, pathG, dim)
            while not completePath:
                if len(pathG) == 0 and startCoord == 'begin':
                    beginRow, beginCol = gInitialInt[0][0], gInitialInt[0][1] #Coordenada del punto inicial
                    elementsAdd = availableAdj(board, currentColor, beginRow, beginCol)
                    #print('Adyacentes: ', elementsAdd)
                elif len(pathG) == 0 and startCoord == 'end':
                    endRow, endCol = gInitialInt[1][0], gInitialInt[1][1] #Coordenada del punto inicial
                    elementsAdd = availableAdjComplete(board, currentColor, endRow, endCol)
                else: 
                    currentCoor = pathG[-1] #Obtener coordenada de la última casilla
                    currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                    if startCoord == 'begin':
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    else:
                        elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 1 and (board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor or board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor+'!'):
                        if pathG not in gRecord:
                            copyPath = pathG.copy()
                            gRecord.append(copyPath)
                        ind = -1
                        for i in range(len(pathG)-1, -1, -1):
                            if len(availableAdj(board, currentColor, int(pathG[i][0]), int(pathG[i][1]))) != 0:
                                ind = i 
                                i = -1
                        if ind != -1:
                            visited.append([int(pathG[ind+1][0]), int(pathG[ind+1][1])])
                            removeNext(currentColor, pathG[ind], board)
                        if len(pathG) == 0:
                            currentCoor = gInitial[0]
                        else:
                            currentCoor = pathG[-1]
                        currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 0:
                        if not checkPath(gInitial, pathG, dim):
                            lastCoor = currentCoor
                            pathG.remove(currentCoor)
                            board[currentRow][currentCol] = '0'
                            if len(pathG) == 0:
                                currentCoor = gInitial[0]
                            else:
                                currentCoor = pathG[-1]
                            currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                            if startCoord == 'begin':
                                elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                            else:
                                elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                            if [int(lastCoor[0]), int(lastCoor[1])] in elementsAdd:
                                elementsAdd.remove([int(lastCoor[0]), int(lastCoor[1])])
                            #end if
                            for v in visited:
                                if v in elementsAdd:
                                    elementsAdd.remove(v)                             
                #end if
                if len(elementsAdd) > 0:
                    for adj in elementsAdd:
                        if len(visited) == 0:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            #print('Costo ', currentCost, ' en ', adj)
                            priorityQueue.put((currentCost, adj))
                        elif adj not in visited:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            #print('Costo ', currentCost, ' en ', adj)
                            priorityQueue.put((currentCost, adj))
                    #end for
                    if not priorityQueue.empty():
                        element = priorityQueue.get()
                        visited.append(element[1])
                        coordenate = str(element[1][0])+str(element[1][1])
                        checkE(coordenate, board)
                        board[element[1][0]][element[1][1]] = 'G'
                        pathG.append(coordenate)
                        showBoard(board)
                        #time.sleep(1)
                        #Vacíar cola de prioridad
                        priorityQueue.queue.clear()
                else:
                    startCoord = 'end'
                    if len(pathG) > 0:
                        checkE(pathG[0], board)
                    #end if
                    visited.clear()
                if checkPath(gInitial, pathG, dim):
                    if pathG not in gRecord:
                        copyPath = pathG.copy()
                        gRecord.append(copyPath)
                    completePath = True
                #end if
            #end while 
            if checkPath(gInitial, pathG, dim):
                countColor += 1
        #end if
        if currentColor == 'W':
            visited = []#'Nodos' visitados en el path
            startCoord = 'begin'
            completePath = checkPath(wInitial, pathW, dim)
            while not completePath:
                if len(pathW) == 0 and startCoord == 'begin':
                    beginRow, beginCol = wInitialInt[0][0], wInitialInt[0][1] #Coordenada del punto inicial
                    elementsAdd = availableAdj(board, currentColor, beginRow, beginCol)
                elif len(pathW) == 0 and startCoord == 'end':
                    endRow, endCol = wInitialInt[1][0], wInitialInt[1][1] #Coordenada del punto inicial
                    elementsAdd = availableAdjComplete(board, currentColor, endRow, endCol)
                else: 
                    currentCoor = pathW[-1] #Obtener coordenada de la última casilla
                    currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                    if startCoord == 'begin':
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    else:
                        elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 1 and (board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor or board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor+'!'):
                        if pathW not in wRecord:
                            copyPath = pathW.copy()
                            wRecord.append(copyPath)
                        ind = -1
                        for i in range(len(pathW)-1, -1, -1):
                            if len(availableAdj(board, currentColor, int(pathW[i][0]), int(pathW[i][1]))) != 0:
                                ind = i 
                                i = -1
                        if ind != -1:
                            visited.append([int(pathW[ind+1][0]), int(pathW[ind+1][1])])
                            removeNext(currentColor, pathW[ind], board)
                        if len(pathW) == 0:
                            currentCoor = wInitial[0]
                        else:
                            currentCoor = pathW[-1]
                        currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 0:
                        if not checkPath(wInitial, pathW, dim):
                            lastCoor = currentCoor
                            pathW.remove(currentCoor)
                            board[currentRow][currentCol] = '0'
                            if len(pathW) == 0:
                                currentCoor = wInitial[0]
                            else:
                                currentCoor = pathW[-1]
                            currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                            if startCoord == 'begin':
                                elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                            else:
                                elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                            if [int(lastCoor[0]), int(lastCoor[1])] in elementsAdd:
                                elementsAdd.remove([int(lastCoor[0]), int(lastCoor[1])])
                            #end if
                            for v in visited:
                                if v in elementsAdd:
                                    elementsAdd.remove(v) 
                #end if
                #print('Adyacentes ', elementsAdd)
                if len(elementsAdd) > 0:
                    for adj in elementsAdd:
                        if len(visited) == 0:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            #print('Costo actual ', currentCost, ' de ', adj)
                            priorityQueue.put((currentCost, adj))
                        elif adj not in visited:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            #print('Costo actual ', currentCost, ' de ', adj)
                            priorityQueue.put((currentCost, adj))
                    #end for
                    if not priorityQueue.empty():
                        element = priorityQueue.get()
                        #print('Elemento ', element)
                        visited.append(element[1])
                        coordenate = str(element[1][0])+str(element[1][1])
                        checkE(coordenate, board)
                        board[element[1][0]][element[1][1]] = 'W'
                        pathW.append(coordenate)
                        showBoard(board)
                        #time.sleep(1)
                        #Vacíar cola de prioridad
                        priorityQueue.queue.clear()
                else:
                    startCoord = 'end'
                    if len(pathW) > 0:
                        checkE(pathW[0], board)
                    #end if
                    visited.clear()
                if checkPath(wInitial, pathW, dim):
                    if pathW not in wRecord:
                        copyPath = pathW.copy()
                        wRecord.append(copyPath)
                    completePath = True
                #end if
            #end while 
            if checkPath(wInitial, pathW, dim):
                countColor += 1
        #end if
        if currentColor == 'C':
            visited = []#'Nodos' visitados en el path
            startCoord = 'begin'
            completePath = checkPath(cInitial, pathC, dim)
            while not completePath:
                if len(pathC) == 0 and startCoord == 'begin':
                    beginRow, beginCol = cInitialInt[0][0], cInitialInt[0][1] #Coordenada del punto inicial
                    elementsAdd = availableAdj(board, currentColor, beginRow, beginCol)
                elif len(pathC) == 0 and startCoord == 'end':
                    endRow, endCol = cInitialInt[1][0], cInitialInt[1][1] #Coordenada del punto inicial
                    elementsAdd = availableAdjComplete(board, currentColor, endRow, endCol)
                else: 
                    currentCoor = pathC[-1] #Obtener coordenada de la última casilla
                    currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                    if startCoord == 'begin':
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    else:
                        elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                    #print('Ady ', elementsAdd)
                    if len(elementsAdd) == 1 and (board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor or board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor+'!'):
                        if pathC not in cRecord:
                            copyPath = pathC.copy()
                            cRecord.append(copyPath)
                        #print('PATH C ', pathC)
                        ind = -1
                        for i in range(len(pathC)-1, -1, -1):
                            #print('PATH C, última pos ', pathC[i])
                            #print('PATH C ', pathC[i][0])
                            if len(availableAdj(board, currentColor, int(pathC[i][0]), int(pathC[i][1]))) != 0:
                                #print('Entra con ', pathC[i])
                                ind = i 
                                i = -1
                        if ind != -1:
                            visited.append([int(pathC[ind+1][0]), int(pathC[ind+1][1])])
                            removeNext(currentColor, pathC[ind], board)
                        #print('PATH SALIR ', pathC)
                        if len(pathC) == 0:
                            currentCoor = cInitial[0]
                        else:
                            currentCoor = pathC[-1]
                        currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 0:
                        if not checkPath(cInitial, pathC, dim):
                            lastCoor = currentCoor
                            pathC.remove(currentCoor)
                            board[currentRow][currentCol] = '0'
                            if len(pathC) == 0:
                                currentCoor = cInitial[0]
                            else:
                                currentCoor = pathC[-1]
                            currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                            if startCoord == 'begin':
                                elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                            else:
                                elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                            if [int(lastCoor[0]), int(lastCoor[1])] in elementsAdd:
                                elementsAdd.remove([int(lastCoor[0]), int(lastCoor[1])])
                            #end if
                            for v in visited:
                                if v in elementsAdd:
                                    elementsAdd.remove(v) 

                #end if
                if len(elementsAdd) > 0:
                    for adj in elementsAdd:
                        if len(visited) == 0:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            priorityQueue.put((currentCost, adj))
                        elif adj not in visited:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            priorityQueue.put((currentCost, adj))
                    #end for
                    if not priorityQueue.empty():
                        element = priorityQueue.get()
                        visited.append(element[1])
                        coordenate = str(element[1][0])+str(element[1][1])
                        checkE(coordenate, board)
                        board[element[1][0]][element[1][1]] = 'C'
                        pathC.append(coordenate)
                        showBoard(board)
                        #time.sleep(1)
                        #Vacíar cola de prioridad
                        priorityQueue.queue.clear()
                else:
                    startCoord = 'end'
                    if len(pathC) > 0:
                        checkE(pathC[0], board)
                    #end if
                    visited.clear()
                if checkPath(cInitial, pathC, dim):  
                    if pathC not in cRecord:
                        copyPath = pathC.copy()
                        cRecord.append(copyPath)                  
                    completePath = True
                #end if
            #end while 
            if checkPath(cInitial, pathC, dim):
                countColor += 1
        #end if
        if currentColor == 'P':
            visited = []#'Nodos' visitados en el path
            startCoord = 'begin'
            completePath = checkPath(pInitial, pathP, dim)
            while not completePath:
                if len(pathP) == 0 and startCoord == 'begin':
                    beginRow, beginCol = pInitialInt[0][0], pInitialInt[0][1] #Coordenada del punto inicial
                    elementsAdd = availableAdj(board, currentColor, beginRow, beginCol)
                elif len(pathP) == 0 and startCoord == 'end':
                    endRow, endCol = pInitialInt[1][0], pInitialInt[1][1] #Coordenada del punto inicial
                    elementsAdd = availableAdjComplete(board, currentColor, endRow, endCol)
                else: 
                    currentCoor = pathP[-1] #Obtener coordenada de la última casilla
                    currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                    if startCoord == 'begin':
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    else:
                        elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 1 and (board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor or board[elementsAdd[0][0]][elementsAdd[0][1]] == currentColor+'!'):
                        if pathP not in pRecord:
                            copyPath = pathP.copy()
                            pRecord.append(copyPath)
                        ind = -1
                        for i in range(len(pathP)-1, -1, -1):
                            if len(availableAdj(board, currentColor, int(pathP[i][0]), int(pathP[i][1]))) != 0:
                                ind = i 
                                i = -1
                        if ind != -1:
                            visited.append([int(pathP[ind+1][0]), int(pathP[ind+1][1])])
                            removeNext(currentColor, pathP[ind], board)
                        if len(pathP) == 0:
                            currentCoor = pInitial[0]
                        else:
                            currentCoor = pathP[-1]
                        currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                        elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                    if len(elementsAdd) == 0:
                        if not checkPath(pInitial, pathP, dim):
                            lastCoor = currentCoor
                            pathP.remove(currentCoor)
                            board[currentRow][currentCol] = '0'
                            if len(pathP) == 0:
                                currentCoor = pInitial[0]
                            else:
                                currentCoor = pathP[-1]
                            currentRow, currentCol = int(currentCoor[0]), int(currentCoor[1])
                            if startCoord == 'begin':
                                elementsAdd = availableAdj(board, currentColor, currentRow, currentCol)
                            else:
                                elementsAdd = availableAdjComplete(board, currentColor, currentRow, currentCol)
                            if [int(lastCoor[0]), int(lastCoor[1])] in elementsAdd:
                                elementsAdd.remove([int(lastCoor[0]), int(lastCoor[1])])
                            #end if
                            for v in visited:
                                if v in elementsAdd:
                                    elementsAdd.remove(v) 
                #end if
                if len(elementsAdd) > 0:
                    for adj in elementsAdd:
                        if len(visited) == 0:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            priorityQueue.put((currentCost, adj))
                        elif adj not in visited:
                            currentCost = cost(board, currentColor, adj[0], adj[1], startCoord)
                            priorityQueue.put((currentCost, adj))
                    #end for
                    if not priorityQueue.empty():
                        element = priorityQueue.get()
                        visited.append(element[1])
                        coordenate = str(element[1][0])+str(element[1][1])
                        checkE(coordenate, board)
                        board[element[1][0]][element[1][1]] = 'P'
                        pathP.append(coordenate)
                        showBoard(board)
                        #time.sleep(1)
                        #Vacíar cola de prioridad
                        priorityQueue.queue.clear()
                else:
                    startCoord = 'end'
                    if len(pathP) > 0:
                        checkE(pathP[0], board)
                    #end if
                    visited.clear()
                if checkPath(pInitial, pathP, dim):
                    if pathP not in pRecord:                        
                        copyPath = pathP.copy()
                        pRecord.append(copyPath)
                    completePath = True
                #end if
            #end while 
            if checkPath(pInitial, pathP, dim):
                countColor += 1
        #end if
    #end while
    resetGame()
    resetActual()
#end def