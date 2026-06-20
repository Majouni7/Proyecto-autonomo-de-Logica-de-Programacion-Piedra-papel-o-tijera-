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


##Se pregunta al jugador si desea volver a jugar##
    volver_a_la_partida = input("¿Desea jugar de nuevo? ")
    
##En esta parte se aplica el bucle para volver a jugar
    if volver_a_la_partida == "si":
        continuar = "si"

##En este caso no se aplicaria el bucle y se terminaria el juego##
    elif volver_a_la_partida =="no":
        continuar = "no"
        print ("Salir del juego")
