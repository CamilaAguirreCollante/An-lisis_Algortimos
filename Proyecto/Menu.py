"""
    Autores: 
        María Camila Aguirre Collante
        Jessica Tatiana Naizaque Guevara
"""
from Interface import *
from Solver import *
'''
Menú de juego -> muestra las intrucciones al jugador
'''
def gameMenu():
    salir = False
    while not salir:
        print("\t\t\tBienvenido/a a Flow Free!")
        print("\tLos tamaños disponibles para el tablero son: ")
        print("\t\t1. 5x5")
        print("\t\t2. 6x6")
        print("\t\t3. 7x7")
        print("\t\t4. 8x8")
        print("\t\t5. Salir")
        option = int(input("\tPor favor elija el tamaño del tablero: "))
        if option == 1:
            play = str(input("\n\t\tDesea jugar? (S/N) "))
            if play.upper() == 'S':
                board = createBoard(5)
                showBoard(board)
                selectMove(board)
            else:
                print("\t\t\t Solucionador por A* modificado \n\n")
                board = createBoard(5)
                showBoard(board)
                bestPath(board)
        elif option == 2:
            play = str(input("\n\t\tDesea jugar? (S/N) "))
            if play.upper() == 'S':
                board = createBoard(6)
                showBoard(board)
                selectMove(board)
            else:
                print("\t\t\t Solucionador por A* modificado \n\n")
                board = createBoard(6)
                showBoard(board)
                bestPath(board)
        elif option == 3:
            play = str(input("\n\t\tDesea jugar? (S/N) "))
            if play.upper() == 'S':
                board = createBoard(7)
                showBoard(board)
                selectMove(board)
            else:
                print("\t\t\t Solucionador por A* modificado \n\n")
                board = createBoard(7)
                showBoard(board)
                bestPath(board)
        elif option == 4:
            play = str(input("\n\t\tDesea jugar? (S/N) "))
            if play.upper() == 'S':
                board = createBoard(8)
                showBoard(board)
                selectMove(board)
            else:
                print("\t\t\t Solucionador por A* modificado \n\n")
                board = createBoard(8)
                showBoard(board)
                bestPath(board)
        elif option == 5:
            print("\n\t\tAdiósss:(\n")
            salir = True
        else: 
            print("\n\t\tOpción inválida!\n")
        print("\n\n")
    #end-while
#end-def

gameMenu()