jugador1 = ""
jugador2 = ""
puntos_j1 = 0
puntos_j2 = 0
juegos_j1 = 0
juegos_j2 = 0
sets_j1 = 0
sets_j2 = 0
saque = 1

# Funcion que calcula los puntos
def calcula_marcador(puntos_j1, puntos_j2):
    marcador_j1 = "0"
    marcador_j2 = "0"
    if puntos_j1 == 1:
        marcador_j1 = "15"
    elif puntos_j1 == 2:
        marcador_j1 = "30"
    elif puntos_j1 == 3:
        marcador_j1 = "40"
    elif puntos_j1 == 4:
        marcador_j1 = "Adv"
    
    if puntos_j2 == 1:
        marcador_j2 = "15"
    elif puntos_j2 == 2:
        marcador_j2 = "30"
    elif puntos_j2 == 3:
        marcador_j2 = "40"
    elif puntos_j2 == 4:
        marcador_j2 = "Adv"

    return marcador_j1 + " - " + marcador_j2


while True:
    try:
        jugador1 = input("Nombre del jugador 1: ")
        jugador2 = input("Nombre del jugador 2: ")
    except:
        print("Nombre de jugador no válido")
        continue
    break

while sets_j1 < 2 and sets_j2 < 2:
    while (juegos_j1 < 6 and juegos_j2 < 6) or abs(juegos_j1 - juegos_j2) < 2:
        while puntos_j1 < 5 and puntos_j2 < 5:
            print()
            print("Sets:   ", sets_j1, "-", sets_j2)
            print("Juegos: ", juegos_j1, "-", juegos_j2)
            print("Puntos: ", calcula_marcador(puntos_j1, puntos_j2))
            print("Saca " + (jugador1 if saque == 1 else jugador2))
            print()

            try:
                punto = input("Punto para (1 ó 2): ")
            except:
                print("Entrada no válida")
                continue

            if punto == "1":
                puntos_j1 += 1
            elif punto == "2":
                puntos_j2 += 1
            elif punto == "s":
                exit()
            else:
                print("Entrada no válida")
                continue

            if puntos_j1 == 4 and puntos_j2 < 3:
                break
            elif puntos_j2 == 4 and puntos_j1 < 3:
                break
            elif puntos_j1 == 4 and puntos_j2 == 4:
                puntos_j1 = 3
                puntos_j2 = 3

        if puntos_j1 > puntos_j2:
            juegos_j1 += 1
        else:
            juegos_j2 += 1
        puntos_j1 = 0
        puntos_j2 = 0
        if saque == 1:
            saque = 2
        else:
            saque = 1
        if (juegos_j1 + juegos_j2) % 2 == 1:
            print("\nCAMBIO DE CANCHA")

    if juegos_j1 > juegos_j2:
        sets_j1 += 1
    else:
        sets_j2 += 1
    juegos_j1 = 0
    juegos_j2 = 0

print()
print("Sets:   ", sets_j1, "-", sets_j2)
if sets_j1 > sets_j2:
    print("Ganador: ", jugador1)
else:
    print("Ganador: ", jugador2)