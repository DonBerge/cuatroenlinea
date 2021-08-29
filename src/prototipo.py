class Tablero:
    def __init__(self, secuencia=None):
        self.tablero = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]

        self.width = 7
        self.height = 6

        if(secuencia != None):
            ficha = 1
            for i in secuencia:
                self.soltarFichaEnColumna(ficha, i)
                ficha = (ficha % 2)+1

    def contenidoColumna(self, nro_columna):
        return [fila[nro_columna-1] for fila in self.tablero]

    def contenidoFila(self, nro_fila):
        return self.tablero[nro_fila-1]

    def filas(self):
        return self.tablero

    def columnas(self):
        return [self.contenidoColumna(x) for x in range(1, self.width+1)]

    def soltarFichaEnColumna(self, ficha, columna):
        [fila for fila in reversed(self.tablero) if fila[columna-1] == 0][0][columna-1] = ficha

    def __str__(self):
        tablero_string = ""
        for fila in self.tablero:
            tablero_string += "| "

            for ficha in fila:
                if(ficha):
                    tablero_string += str(ficha)
                else:
                    tablero_string += ' '
                tablero_string += ' '

            tablero_string += "|\n"

        tablero_string += '+'
        for i in range(self.width*2+1):
            tablero_string += '-'
        tablero_string += '+'

        return tablero_string

#################################################################


def esSecuenciaValida(secuencia):
    elementos_validos = [columna for columna in secuencia if 1 <= columna <= 7]
    return len(elementos_validos) == len(secuencia)


if __name__ == "__main__":
    secuencia = [1, 2, 3, 4, 5, 6, 7, 4,4]

    if(esSecuenciaValida(secuencia)):
        tablero = Tablero(secuencia)
        print(tablero)
    else:
        print("Secuencia no valida, las columnas tienen que estar entre el 1 y el 7")
