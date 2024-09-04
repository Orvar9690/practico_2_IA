# Main.py

import time
from ciudad import Ciudad
from BFS import BFS_Ponderado
from DFS import DFS_Ponderado
from A_Star import AStar_Ponderado

if __name__ == "__main__":
    # Crear una instancia de la clase Ciudad
    # Descargamos el grafo de la ciudad especificada
    mi_ciudad = Ciudad("Buenos Aires, Argentina")
    print("Arrancando...")
    mi_ciudad.descargar_grafo()
    print("Grafo descargado....")
    print("Creando visualización.....")
    mi_ciudad.visualizar_grafo()
    print("Visualización lista......")


    # Elegir nodos de inicio y objetivo
    # Tomamos dos nodos arbitrarios del grafo como punto de partida y destino
    nodo_inicio = list(mi_ciudad.graf().keys())[0]
    nodo_objetivo = list(mi_ciudad.graf().keys())[20]

    # Ejecutar y medir BFS
    # Realizamos la búsqueda usando BFS Ponderado y medimos el tiempo de ejecución
    print("Usando BFS")
    bfs = BFS_Ponderado(mi_ciudad)
    tiempo_inicio = time.time()
    camino_bfs, nodos_recorridos_bfs = bfs.buscar(nodo_inicio, nodo_objetivo)
    tiempo_fin = time.time()
    duracion_bfs = tiempo_fin - tiempo_inicio

    # Ejecutar y medir DFS
    # Realizamos la búsqueda usando DFS Ponderado y medimos el tiempo de ejecución
    print("Usando DFS")
    dfs = DFS_Ponderado(mi_ciudad)
    tiempo_inicio = time.time()
    camino_dfs, nodos_recorridos_dfs = dfs.buscar(nodo_inicio, nodo_objetivo)
    tiempo_fin = time.time()
    duracion_dfs = tiempo_fin - tiempo_inicio

    # Ejecutar y medir A*
    # Realizamos la búsqueda usando A* Ponderado y medimos el tiempo de ejecución
    print("Usando Astar")
    astar = AStar_Ponderado(mi_ciudad)
    tiempo_inicio = time.time()
    camino_astar, nodos_recorridos_astar = astar.buscar(nodo_inicio, nodo_objetivo)
    tiempo_fin = time.time()
    duracion_astar = tiempo_fin - tiempo_inicio

    # Mostrar resultados
    # Aquí imprimimos los resultados de cada algoritmo
    print("\nBFS Ponderado")
    print(f"Camino: {camino_bfs}")
    print(f"Tiempo de ejecución: {duracion_bfs:.6f} segundos")
    print(f"Número de nodos recorridos: {nodos_recorridos_bfs}")

    print("\nDFS Ponderado")
    print(f"Camino: {camino_dfs}")
    print(f"Tiempo de ejecución: {duracion_dfs:.6f} segundos")
    print(f"Número de nodos recorridos: {nodos_recorridos_dfs}")

    print("\nA* Ponderado")
    print(f"Camino: {camino_astar}")
    print(f"Tiempo de ejecución: {duracion_astar:.6f} segundos")
    print(f"Número de nodos recorridos: {nodos_recorridos_astar}")
