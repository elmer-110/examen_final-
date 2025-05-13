import unittest
from ejercicio.cuantica.estado_cuantico import EstadoCuantico
from ejercicio.cuantica.operador_cuantico import OperadorCuantico

class TestOperadorCuantico(unittest.TestCase):
    def test_aplicar_x(self):
        estado = EstadoCuantico("q0", [1, 0], "computacional")
        x = OperadorCuantico("X", [[0, 1], [1, 0]])
        resultado = x.aplicar(estado)
        self.assertAlmostEqual(resultado.vector[0], 0.0 + 0j)
        self.assertAlmostEqual(resultado.vector[1], 1.0 + 0j)
