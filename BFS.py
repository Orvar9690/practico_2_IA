# BFS.py

import heapq

class BFS_Ponderado:
    def __init__(self, ciudad):
        self.ciudad = ciudad  # Guardamos la referencia a la ciudad

    # Implementación del algoritmo BFS Ponderado
    def buscar(self, inicio, objetivo):
        grafo = self.ciudad.graf()  # Obtenemos el grafo como diccionario
        cola = []
        heapq.heappush(cola, (0, inicio))  # Inicializamos la cola de prioridad
        costos = {nodo: float('inf') for nodo in grafo}
        costos[inicio] = 0
        padres = {inicio: None}
        nodos_recorridos = 0

        while cola:
            costo_actual, nodo_actual = heapq.heappop(cola)
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
                    heapq.heappush(cola, (nuevo_costo, vecino))

        return None, nodos_recorridos  # Devolvemos None si no se encontró el camino
