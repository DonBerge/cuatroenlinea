from src.prototipo import columnas, completarTableroEnOrden, contenidoColumna, contenidoFila, esSecuenciaValida, soltarFichaEnColumna, tableroVacio, filas

tablero_vacio=tableroVacio()

tablero_medio_lleno = [
        [0, 0, 0, 0, 0, 2, 1],
        [0, 0, 0, 0, 1, 2, 1],
        [0, 0, 0, 1, 2, 1, 2],
        [0, 0, 2, 1, 2, 1, 2],
        [0, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ]

columnas_tablero_medio_lleno = [
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 2, 2],
        [0, 0, 0, 2, 1, 1],
        [0, 0, 1, 1, 2, 2],
        [0, 1, 2, 2, 1, 1],
        [2, 2, 1, 1, 2, 2],
        [1, 1, 2, 2, 1, 1]
    ]

secuencia_tablero_medio_lleno = [1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 4, 5, 6, 7, 5, 6, 7, 6, 7]

tablero_completo = completarTableroEnOrden(secuencia_tablero_medio_lleno,tableroVacio())

def test_esSecuenciaValida():
    assert(esSecuenciaValida(secuencia_tablero_medio_lleno))

def test_esSecuenciaInvalida():
    assert not esSecuenciaValida([-1,1,-10,3,5])
    assert not esSecuenciaValida([1,7,9,2])

def test_completar_tablero_en_orden():
    assert(tablero_completo == tablero_medio_lleno)

def test_contenidoFila():
    for i in range(6):
        assert tablero_medio_lleno[i]==contenidoFila(i+1,tablero_medio_lleno)

def test_contenidoColumna():
    for i in range(7):
        assert columnas_tablero_medio_lleno[i] == contenidoColumna(i+1,tablero_medio_lleno)

def test_soltarFichaEnColumna():
    tablero = tableroVacio()
    for i in range(6):
        soltarFichaEnColumna(1,3,tablero)
        soltarFichaEnColumna(2,4,tablero)
    assert [1,1,1,1,1,1] == contenidoColumna(3,tablero)
    assert [2,2,2,2,2,2] == contenidoColumna(4,tablero)

def test_filas():
    assert tablero_medio_lleno == filas(tablero_medio_lleno)

def test_columnas():
    assert columnas_tablero_medio_lleno == columnas(tablero_medio_lleno)

def test_tablero_vacio_tiene_6_filas():
    assert(len(tablero_vacio)==6)

def test_tablero_vacio_tiene_7_columnas():
    assert(len(tablero_vacio[0])==7)

def test_tablero_vacio_esta_vacio():
    fila_vacia = [0,0,0,0,0,0,0]
    for i in range(6):
        assert(tablero_vacio[i]==fila_vacia)


