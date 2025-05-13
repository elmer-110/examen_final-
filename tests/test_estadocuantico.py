
import unittest
from ejercicio.cuantica.estado_cuantico import EstadoCuantico

class TestEstadoCuantico(unittest.TestCase):
    def test_medicion_basica(self):
        estado = EstadoCuantico("test", [1, 0], "computacional")
        probs = estado.medir()
        self.assertAlmostEqual(probs["0"], 1.0)
        self.assertAlmostEqual(probs["1"], 0.0)

    def test_normalizacion_invalida(self):
        with self.assertRaises(ValueError):
            EstadoCuantico("mal", [0.5, 0.5], "computacional")  # No normalizado
