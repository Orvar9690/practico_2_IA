# ciudad.py

import osmnx as ox
import matplotlib.pyplot as plt

class Ciudad:
    def __init__(self, lugar):
        self.lugar = lugar  # Nombre del lugar para el que se descargará el grafo
        self.grafo = None  # Aquí se almacenará el grafo descargado
        self.grafo_diccionario = None  # Aquí se almacenará el grafo convertido en diccionario

    def descargar_grafo(self):
        # Descargar el grafo de calles del lugar especificado usando OSMnx
        self.grafo = ox.graph_from_place(self.lugar, network_type='drive')

    def visualizar_grafo(self, figsize=(68, 68)):
        if self.grafo is None:
            raise ValueError("El grafo no ha sido descargado. Llama a 'descargar_grafo' primero.")

        # Crear una figura de matplotlib con el tamaño especificado
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_facecolor('black')  # Establecer el fondo negro

        # Dibujar el grafo con las personalizaciones deseadas
        ox.plot_graph(
            self.grafo,
            ax=ax,
            node_size=100000,  # Tamaño de los nodos
            node_color='blue',  # Color de los nodos
            node_edgecolor='none',  # Sin borde en los nodos
            node_zorder=1,  # Los nodos se dibujan debajo de las aristas
            edge_color='gray',  # Color de las aristas
            edge_linewidth=0.5,  # Grosor de las aristas
            edge_alpha=1.0,  # Transparencia de las aristas
            bgcolor='black',  # Color de fondo de la gráfica
        )

        # Mostrar la figura generada
        plt.show()

    def graf(self):
        if self.grafo is None:
            raise ValueError("El grafo no ha sido descargado. Llama a 'descargar_grafo' primero.")

        # Convertir el grafo a un diccionario donde las llaves son los nodos
        # y los valores son listas de tuplas (nodo_vecino, peso de la arista)
        self.grafo_diccionario = {}

        # Iterar sobre las aristas del grafo para crear el diccionario
        for u, v, data in self.grafo.edges(data=True):
            peso = data['length']  # Usar la longitud de la arista como peso

            # Asegurarse de que ambos nodos están en el diccionario
            if u not in self.grafo_diccionario:
                self.grafo_diccionario[u] = []
            if v not in self.grafo_diccionario:
                self.grafo_diccionario[v] = []

            # Añadir las conexiones bidireccionales
            self.grafo_diccionario[u].append((v, peso))
            self.grafo_diccionario[v].append((u, peso))

        return self.grafo_diccionario  # Devolver el diccionario con el grafo
