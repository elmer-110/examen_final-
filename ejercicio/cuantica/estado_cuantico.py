import numpy as np
from typing import List, Union, Dict

class EstadoCuantico:
    def __init__(self, identificador: str, vector: List[Union[float, complex]], base: str = "computacional"):
        if not vector:
            raise ValueError("El vector de estado no puede estar vacío.")
        self.id = identificador
        self.vector = np.array(vector, dtype=complex)
        self.base = base

        # Validación de normalización
        probabilidad_total = np.sum(np.abs(self.vector) ** 2)
        if not np.isclose(probabilidad_total, 1.0, atol=1e-6):
            raise ValueError("El vector de estado no está normalizado (∑|amplitudes|² ≠ 1).")

    def medir(self) -> Dict[str, float]:
        probabilidades = np.abs(self.vector) ** 2
        return {str(i): round(float(p), 6) for i, p in enumerate(probabilidades)}

    def __str__(self):
        return f"{self.id}: vector={self.vector.tolist()} en base {self.base}"

    def __repr__(self):
        return self.__str__()
