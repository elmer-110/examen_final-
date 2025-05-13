import os
import json
from typing import List, Union
from .estado_cuantico import EstadoCuantico
from .operador_cuantico import OperadorCuantico

class RepositorioDeEstados:
    def __init__(self):
        self.estados = {}

    def listar_estados(self) -> List[str]:
        if not self.estados:
            return ["No hay estados registrados."]
        return [str(estado) for estado in self.estados.values()]

    def agregar_estado(self, identificador: str, vector: List[Union[float, complex]], base: str):
        if identificador in self.estados:
            raise ValueError(f"Error: ya existe un estado con identificador '{identificador}'.")
        estado = EstadoCuantico(identificador, vector, base)
        self.estados[identificador] = estado

    def obtener_estado(self, identificador: str) -> EstadoCuantico:
        if identificador not in self.estados:
            raise KeyError(f"No se encontró el estado con identificador '{identificador}'.")
        return self.estados[identificador]

    def eliminar_estado(self, identificador: str):
        if identificador not in self.estados:
            raise KeyError(f"No se puede eliminar: estado '{identificador}' no encontrado.")
        del self.estados[identificador]

    def aplicar_operador(self, id_estado: str, operador: OperadorCuantico, nuevo_id: str = None) -> EstadoCuantico:
        if id_estado not in self.estados:
            raise KeyError(f"No existe el estado con id '{id_estado}' en el repositorio.")
        estado_original = self.estados[id_estado]
        if operador.matriz.shape[1] != estado_original.vector.shape[0]:
            raise ValueError("Dimensiones incompatibles entre el operador y el estado.")
        nuevo_estado = operador.aplicar(estado_original)

        if nuevo_id:
            nuevo_estado.id = nuevo_id
        else:
            nuevo_estado.id = f"{estado_original.id}_{operador.nombre}"

        if nuevo_estado.id in self.estados:
            raise ValueError(f"Ya existe un estado con id '{nuevo_estado.id}' en el repositorio.")

        self.estados[nuevo_estado.id] = nuevo_estado
        return nuevo_estado

    def medir_estado(self, identificador: str) -> str:
        estado = self.obtener_estado(identificador)
        probabilidades = estado.medir()
        salida = [f"Medición del estado {estado.id} (base {estado.base}):"]
        for base_i, prob in probabilidades.items():
            porcentaje = round(prob * 100, 2)
            salida.append(f"  - Estado base {base_i}: {porcentaje}%")
        return "\n".join(salida)

    def guardar(self, archivo: str):
        lista_estados = []
        for estado in self.estados.values():
            lista_estados.append({
                "id": estado.id,
                "base": estado.base,
                "vector": [complex(a).real if a.imag == 0 else [a.real, a.imag] for a in estado.vector.tolist()]
            })
        with open(archivo, mode='w') as file:
            json.dump(lista_estados, file, indent=4)
        return f"Estados guardados en {archivo} ({len(lista_estados)} estados)."

    def cargar(self, archivo: str):
        if not os.path.exists(archivo):
            raise FileNotFoundError(f"No se encontró el archivo '{archivo}'.")
        with open(archivo) as file:
            lista_estados = json.load(file)
        self.estados.clear()
        for estado_data in lista_estados:
            id = estado_data["id"]
            base = estado_data["base"]
            vector_raw = estado_data["vector"]
            vector = [complex(*v) if isinstance(v, list) else complex(v, 0) for v in vector_raw]
            self.agregar_estado(id, vector, base)
        return f"{len(lista_estados)} estados cargados desde {archivo}."
