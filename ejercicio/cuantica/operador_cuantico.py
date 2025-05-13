import numpy as np
from typing import List, Union
from .estado_cuantico import EstadoCuantico

class OperadorCuantico:
    def __init__(self, nombre: str, matriz: List[List[Union[float, complex]]]):
        self.nombre = nombre
        self.matriz = np.array(matriz, dtype=complex)

        if self.matriz.shape[0] != self.matriz.shape[1]:
            raise ValueError("La matriz del operador debe ser cuadrada.")

    def aplicar(self, estado: EstadoCuantico) -> EstadoCuantico:
        if self.matriz.shape[1] != estado.vector.shape[0]:
            raise ValueError("Dimensión del operador incompatible con el estado.")

        nuevo_vector = np.dot(self.matriz, estado.vector)
        nuevo_id = f"{estado.id}_{self.nombre}"
        return EstadoCuantico(nuevo_id, nuevo_vector.tolist(), base=estado.base)

    def __str__(self):
        return f"Operador {self.nombre}: matriz={self.matriz.tolist()}"

    def __repr__(self):
        return self.__str__()
