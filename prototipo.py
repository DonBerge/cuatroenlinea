import sys

sys.stdin = open("input.txt", 'r')
sys.stdout = open("output.txt", 'w')


def tableroVacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def esSecuenciaValida(secuencia):
    for i in secuencia:
        if(not (i>=1 and i<=6)):
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
    for fila in range(0, 6, 1):
        for columna in range(0, 6, 1):
            ficha = tablero[fila][columna]
            if(ficha):
                print(ficha, end=' ')
            else:
                print(end=' ')
        print()


secuencia = list(map(int, input().split()))

if(esSecuenciaValida(secuencia)):
    dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))
else:
    print("Secuencia no valida, las columnas tienen que estar entre el 1 y el 7")
