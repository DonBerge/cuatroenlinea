import sys

def tableroVacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def contenidoColumna(nro_columna,tablero):
    columna = []
    for fila in tablero:
        columna.append(fila[nro_columna-1])
    return columna

def contenidoFila(nro_fila, tablero):
    return tablero[nro_fila-1]

def filas(tablero):
    return tablero

def columnas(tablero):
    array_de_columnas=[]
    for nro_columna in range (7):
        columna = []
        for nro_fila in range(6):
            columna.append(tablero[nro_fila][nro_columna])
        array_de_columnas.append(columna)
    return array_de_columnas

def esSecuenciaValida(secuencia):
    for i in secuencia:
        if(not (i>=1 and i<=7)):
            return False
    return True


def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila-1][columna-1] == 0:
            tablero[fila-1][columna-1] = ficha
            return


def completarTableroEnOrden(secuencia, tablero):
    ficha = 1
    for i in secuencia:
        soltarFichaEnColumna(ficha, i, tablero)
        ficha = (ficha % 2)+1
    return tablero


def dibujarTablero(tablero):
    for fila in range(6):
        print('|',end=' ')
        for columna in range(7):
            ficha = tablero[fila][columna]
            if(ficha):
                print(ficha, end=' ')
            else:
                print(end="  ")
        print('|')
    print('+',end='')
    for i in range(15):
        print('-',end='')
    print('+',end=' ')


secuencia = [1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 4, 5, 6, 7, 5, 6, 7, 6, 7]

tablero=tableroVacio()

if(esSecuenciaValida(secuencia)):
    tablero=completarTableroEnOrden(secuencia, tableroVacio())
    dibujarTablero(tablero)
else:
    print("Secuencia no valida, las columnas tienen que estar entre el 1 y el 7")