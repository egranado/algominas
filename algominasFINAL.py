import random
import string

FILAS = 8
COLUMNAS = 8
MINAS = 10
MINA = "*"
BANDERA = "B"
VACIA = " "
LETRAS_DE_COLUMNAS = string.ascii_uppercase


def algominas():
    '''Función principal del buscaminas.'''
    while True:
        print(f"¡Bienvenido al buscaminas, hay {MINAS} minas que encontrar!")
        tablero = generar_tablero(FILAS, COLUMNAS)
        tablero_de_minas = generar_tablero(FILAS, COLUMNAS)
        colocar_minas(tablero_de_minas)
        imprimir_tablero(tablero)
        while not esta_terminado(tablero):
            if pedir_accion():
                fila, columna = pedir_celda()
                plantar_bandera(tablero, fila, columna)
            else:
                fila, columna = pedir_celda()
                descubrir_celda(tablero, tablero_de_minas, fila, columna)
            imprimir_tablero(tablero)
        print("¡Juego terminado!")
        if not jugar_de_nuevo():
            break


def generar_tablero(filas, columnas):
    '''Crea el tablero de juego.'''
    tablero = []
    for i in range(filas):
        filas = []
        for j in range(columnas):
            filas.append(VACIA)
        tablero.append(filas)
    return tablero


def imprimir_tablero(tablero):
    '''Imprime el tablero.'''
    print("  ", '|'.join(LETRAS_DE_COLUMNAS[:COLUMNAS]))
    for i, filas in enumerate(tablero):
        if i < 10:
            print(i, '|'.join(filas), sep="  ")
        else:
            print(i, '|'.join(filas))


def elegir_celda_al_azar():
    '''Elige una celda del tablero al azar.'''
    return random.randint(0, FILAS - 1), random.randint(0, COLUMNAS - 1)


def colocar_minas(tablero):
    '''Distribuye las minas en el tablero.'''
    minas = 0
    while minas < MINAS:
        fila, columna = elegir_celda_al_azar()
        if tablero[fila][columna] != MINA:
            tablero[fila][columna] = MINA
            minas += 1


def pedir_accion():
    '''Permite al usuario elegir plantar una bandera o descubrir una celda.'''
    opcion = input("Ingrese B para colocar/remover una bandera u otro ingreso para descubrir una celda: ")
    if opcion.upper() == 'B':
        return True
    else:
        return False


def pedir_celda():
    '''Pide un número de fila y columna válido al usuario.'''
    while True:
        elegido = input("Ingrese un número de fila y columna separados por un - (por ejemplo: '3-C'): ")
        celda = elegido.split("-")
        if len(celda) == 2 and (celda[0].isdigit() and int(celda[0]) < FILAS) and (celda[1].upper() in LETRAS_DE_COLUMNAS[:COLUMNAS] and celda[1] != ""):
            return int(celda[0]), LETRAS_DE_COLUMNAS.index(celda[1].upper())


def plantar_bandera(tablero, fila, columna):
    '''Coloca o remueve una bandera en la celda elegida.'''
    while True:
        if tablero[fila][columna] == BANDERA:
            tablero[fila][columna] = VACIA
            break
        elif tablero[fila][columna] == VACIA:
            tablero[fila][columna] = BANDERA
            break
        else:
            break


def calcular_minas_adyacentes(fila, columna, tablero_de_minas):
    '''Calcula la cantidad de minas en las celdas adyacentes a la de referencia.'''
    # En filas me muevo entre [-1, 1] y en columnas también para buscar adyacentes, 0 en ambos rangos es la celda referencia (no me muevo en f ni en c).
    contador = 0
    for f in range(fila - 1, fila + 2):
        for c in range(columna - 1, columna + 2):
            if f == 0 and c == 0:
                continue
            elif f % len(tablero_de_minas) == f and c % len(tablero_de_minas[f]) == c and tablero_de_minas[f][c] == MINA:
                contador += 1
    return contador


def descubrir_celda(tablero, tablero_de_minas, fila, columna):
    '''Descubre una celda e indica la cantidad de minas adyacentes si está vacía.'''
    while True:
        if tablero[fila][columna] == BANDERA:
            break
        elif tablero_de_minas[fila][columna] == MINA:
            tablero[fila][columna] = MINA
            break
        elif tablero[fila][columna] == VACIA:
            minas_adyacentes = calcular_minas_adyacentes(fila, columna, tablero_de_minas)
            tablero[fila][columna] = str(minas_adyacentes)
            break
        else:
            break


def esta_terminado(tablero):
    '''Comprueba si ha terminado el juego.'''
    for i in range(FILAS):
        if MINA in tablero[i]:
            return True
    contador = 0
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if tablero[i][j] not in (BANDERA, VACIA):
                contador += 1
    if FILAS * COLUMNAS - contador == MINAS:
        return True
    return False


def jugar_de_nuevo():
    '''Permite al jugador volver a jugar.'''
    while True:
        eleccion = input("¿Volver a jugar? S/N: ")
        if eleccion.upper() == 'S':
            return True
        elif eleccion.upper() == 'N':
            return False


algominas()