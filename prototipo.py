import sys

sys.stdout = open("output.txt", 'w')
sys.stdin = open("input.txt", 'r')


def tableroVacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]


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
    for fila in range(0, 6, 1):
        for columna in range(0, 6, 1):
            ficha = tablero[fila][columna]
            if(ficha):
                print(ficha, end=' ')
            else:
                print(end=' ')
        print()


secuencia = list(map(int, input().split()))

dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))
