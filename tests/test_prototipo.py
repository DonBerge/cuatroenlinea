from src.prototipo import Tablero, esSecuenciaValida

tablero_vacio=Tablero()

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

tablero_completo = Tablero(secuencia_tablero_medio_lleno)

def test_esSecuenciaValida():
    assert esSecuenciaValida(secuencia_tablero_medio_lleno)

def test_esSecuenciaInvalida():
    assert not esSecuenciaValida([-1,1,-10,3,5])
    assert not esSecuenciaValida([1,7,9,2])

def test_completar_tablero_en_orden():
    assert tablero_completo.filas() == tablero_medio_lleno

def test_contenidoFila():
    if(tablero_completo.height==6):
        for i in range(6):
            assert tablero_medio_lleno[i]==tablero_completo.contenidoFila(i+1)

def test_contenidoColumna():
    if(tablero_completo.width==7):
        for i in range(7):
            assert columnas_tablero_medio_lleno[i] == tablero_completo.contenidoColumna(i+1)

def test_soltarFichaEnColumna():
    tablero = Tablero()
    h = tablero.height
    for i in range(h):
        tablero.soltarFichaEnColumna(1,3)
        tablero.soltarFichaEnColumna(2,4)
    assert [1 for x in range(h)] == tablero.contenidoColumna(3)
    assert [2 for x in range(h)] == tablero.contenidoColumna(4)

def test_filas():
    assert tablero_medio_lleno == tablero_completo.filas()

def test_columnas():
    assert columnas_tablero_medio_lleno == tablero_completo.columnas()

def test_tablero_vacio_tiene_6_filas():
    assert len(tablero_vacio.filas())==tablero_vacio.height

def test_tablero_vacio_tiene_7_columnas():
    assert len(tablero_vacio.columnas())==tablero_vacio.width

def test_tablero_vacio_esta_vacio():
    fila_vacia = [0 for x in range(tablero_vacio.width)]
    for fila in tablero_vacio.filas():
        assert fila==fila_vacia


