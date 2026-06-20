##Juego de piedra, papel o tijera##

##Variable que hace posible el bucle##
continuar = "si"


##El bucle permite repetir el juego si el usuario lo desea##
while continuar == "si":
    
    ##El jugador y el sistema eligen una opción##
    jugador = input("Elige piedra, papel o tijera: ")
    sistema = input("Ingrese la opción del sistema: ")

    
    ##En el caso de que la opción del jugador sea igual a la del sistema##
    if jugador == sistema:
        print("Empate")


    ##Se compara las opciones y se aplican las reglas de juego##
    elif (jugador == "piedra" and sistema == "tijera") or \
         (jugador == "papel" and sistema == "piedra") or \
         (jugador == "tijera" and sistema == "papel"):
        print("Ganaste")


    ##En el caso de que el jugador no gane ni empate, pirde##
    else:
        print("Perdiste")


##Se pregunta al jugador si desea volver a jugar para aplicar el bucle##
    continuar = input("¿Desea jugar de nuevo? (si/no): ")
    
##Si el usuario deside no seguir jugando, finaliza el juego ##
    if continuar == "no":
        print("Salir del juego")