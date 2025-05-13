from cuantica.repositorio import RepositorioDeEstados
from cuantica.operador_cuantico import OperadorCuantico
import numpy as np

def menu():
    repo = RepositorioDeEstados()
    operadores = {
        "X": OperadorCuantico("X", [[0, 1], [1, 0]]),
        "H": OperadorCuantico("H", [[1/np.sqrt(2), 1/np.sqrt(2)],
                                     [1/np.sqrt(2), -1/np.sqrt(2)]])
    }

    while True:
        print("\n=== Simulador Cuántico ===")
        print("1. Listar estados")
        print("2. Agregar nuevo estado")
        print("3. Aplicar operador cuántico")
        print("4. Medir estado")
        print("5. Guardar estados en archivo")
        print("6. Cargar estados desde archivo")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            for linea in repo.listar_estados():
                print(linea)

        elif opcion == "2":
            id = input("Identificador del estado: ")
            base = input("Base (ej: computacional): ")
            vec_str = input("Vector de estado (ej: 1,0 o 0.707,0.707): ")
            try:
                vec = [complex(x.strip()) for x in vec_str.split(",")]
                repo.agregar_estado(id, vec, base)
                print("Estado agregado.")
            except Exception as e:
                print("Error:", e)

        elif opcion == "3":
            estado_id = input("ID del estado a transformar: ")
            print("Operadores disponibles:", list(operadores.keys()))
            op = input("Nombre del operador: ").strip().upper()
            nuevo_id = input("ID del nuevo estado (dejar vacío para automático): ")
            try:
                operador = operadores[op]
                result = repo.aplicar_operador(estado_id, operador, nuevo_id or None)
                print("Estado generado:", result)
            except Exception as e:
                print("Error:", e)

        elif opcion == "4":
            estado_id = input("ID del estado a medir: ")
            try:
                print(repo.medir_estado(estado_id))
            except Exception as e:
                print("Error:", e)

        elif opcion == "5":
            ruta = input("Nombre del archivo (ej: estados.json): ")
            try:
                print(repo.guardar(ruta))
            except Exception as e:
                print("Error al guardar:", e)

        elif opcion == "6":
            ruta = input("Nombre del archivo a cargar: ")
            try:
                print(repo.cargar(ruta))
            except Exception as e:
                print("Error al cargar:", e)

        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
