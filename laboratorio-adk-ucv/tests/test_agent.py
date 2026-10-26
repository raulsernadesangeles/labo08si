
from agente_ucv.agent import explicar_concepto, calcular_promedio


def test_concepto_existente():
    resultado = explicar_concepto("api")
    assert resultado["status"] == "success"


def test_concepto_inexistente():
    resultado = explicar_concepto("desconocido")
    assert resultado["status"] == "not_found"


def test_concepto_vacio():
    resultado = explicar_concepto("")
    assert resultado["status"] == "error"


def test_calcular_promedio():
    resultado = calcular_promedio([15, 18, 17])
    assert resultado["promedio"] == 16.67


def test_promedio_sin_notas():
    resultado = calcular_promedio([])
    assert resultado["status"] == "error"


def test_nota_fuera_de_rango():
    resultado = calcular_promedio([15, 25])
    assert resultado["status"] == "error"
