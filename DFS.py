# DFS.py

class DFS_Ponderado:
    def __init__(self, ciudad):
        self.ciudad = ciudad  # Guardamos la referencia a la ciudad

    # Implementación del algoritmo DFS Ponderado
    def buscar(self, inicio, objetivo):
        grafo = self.ciudad.graf()  # Obtenemos el grafo como diccionario
        pila = [(0, inicio)]
        costos = {nodo: float('inf') for nodo in grafo}
        costos[inicio] = 0
        padres = {inicio: None}
        nodos_recorridos = 0

        while pila:
            costo_actual, nodo_actual = pila.pop()
            nodos_recorridos += 1
            if nodo_actual == objetivo:
                camino = []
                while nodo_actual is not None:
                    camino.append(nodo_actual)
                    nodo_actual = padres[nodo_actual]
                return camino[::-1], nodos_recorridos  # Devolvemos el camino y el número de nodos recorridos

            for vecino, peso in grafo[nodo_actual]:
                nuevo_costo = costo_actual + peso
                if nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    padres[vecino] = nodo_actual
                    pila.append((nuevo_costo, vecino))

        return None, nodos_recorridos  # Devolvemos None si no se encontró el camino
