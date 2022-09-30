"""
    Autores: 
        María Camila Aguirre Collante
        Jessica Tatiana Naizaque Guevara
"""
from InterfazPrueba import *
'''
Menú de juego -> muestra las intrucciones al jugador
'''
def gameMenu():
    salir = False
    print("\t\t\tBienvenido/a a Flow Free!")
    print("\tLos tamaños disponibles para el tablero son: ")
    print("\t\t1. 5x5")
    print("\t\t2. 6x6")
    print("\t\t3. 7x7")
    print("\t\t4. 8x8")
    print("\t\t5. 9x9")
    print("\t\t6. Salir")
    option = int(input("\tPor favor elija el tamaño del tablero: "))
    
    

    while not salir:
        if option == 1:
            board = createBoard(5)
            showBoard(board)
            select_move(board)
            salir = True
        elif option == 2:
            board = createBoard(6)
            showBoard(board)
            salir = True
        elif option == 3:
            board = createBoard(7)
            showBoard(board)
            salir = True
        elif option == 4:
            board = createBoard(8)
            showBoard(board)
            salir = True
        elif option == 5:
            board = createBoard(9)
            showBoard(board)
            salir = True
        elif option == 6:
            salir = True
        else: 
            print("\n\t\tOpción inválida!\n")
            print("\tRecuerde los tamaños disponibles: 5x5(1), 6x6(2), 7x7(3), 8x8(4) y 9x9(5) ")
            option = int(input("\tIngrese de nuevo una opción: "))
        print("\n\n")
    #end-while
#end-def

gameMenu()
