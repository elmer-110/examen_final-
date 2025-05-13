import unittest
import tempfile
import os
from ejercicio.cuantica.repositorio import RepositorioDeEstados
from ejercicio.cuantica.operador_cuantico import OperadorCuantico

class TestRepositorioDeEstados(unittest.TestCase):
    def test_agregar_y_listar(self):
        repo = RepositorioDeEstados()
        repo.agregar_estado("q1", [1, 0], "computacional")
        self.assertIn("q1", repo.estados)
        self.assertEqual(len(repo.listar_estados()), 1)

    def test_prevenir_duplicados(self):
        repo = RepositorioDeEstados()
        repo.agregar_estado("q1", [1, 0], "computacional")
        with self.assertRaises(ValueError):
            repo.agregar_estado("q1", [0, 1], "computacional")

    def test_aplicar_operador(self):
        repo = RepositorioDeEstados()
        repo.agregar_estado("q0", [1, 0], "computacional")
        x = OperadorCuantico("X", [[0, 1], [1, 0]])
        nuevo = repo.aplicar_operador("q0", x, "q0_X")
        self.assertIn("q0_X", repo.estados)
        self.assertAlmostEqual(nuevo.vector[1], 1.0 + 0j)

    def test_guardar_y_cargar_json(self):
        repo = RepositorioDeEstados()
        repo.agregar_estado("q1", [1, 0], "computacional")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
            archivo = tmp.name
            repo.guardar(archivo)

        repo2 = RepositorioDeEstados()
        repo2.cargar(archivo)
        self.assertIn("q1", repo2.estados)
        os.remove(archivo)
