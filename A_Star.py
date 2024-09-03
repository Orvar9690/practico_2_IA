# A_Star.py

import heapq
from math import sqrt


class AStar_Ponderado:
    def __init__(self, ciudad):
        self.ciudad = ciudad  # Guardamos la referencia a la ciudad

    # Esta función calcula la distancia Manhattan entre dos nodos
    def calcular_distancia_euclidiana(self, nodo1, nodo2):
        x1, y1 = self.ciudad.grafo.nodes[nodo1]['x'], self.ciudad.grafo.nodes[nodo1]['y']
        x2, y2 = self.ciudad.grafo.nodes[nodo2]['x'], self.ciudad.grafo.nodes[nodo2]['y']
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Implementación del algoritmo A* Ponderado
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
                return camino[::-1], nodos_recorridos

            for vecino, peso in grafo[nodo_actual]:
                nuevo_costo = costos[nodo_actual] + peso
                heuristica = self.calcular_distancia_euclidiana(vecino, objetivo)  # Aplicamos la heurística
                costo_total = nuevo_costo + heuristica

                if costo_total < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    padres[vecino] = nodo_actual
                    heapq.heappush(cola, (costo_total, vecino))

        return None, nodos_recorridos  # Devolvemos None si no se encontró el camino
