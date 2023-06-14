def bellman_ford(grafo, escolhido):
    # Inicializando as distâncias dos vértices como infinito
    distancias = {vertice: float('inf') for vertice in grafo}
    # Definindo a distância do vértice de origem como 0
    distancias[escolhido] = 0

    # Relaxamento das arestas
    for _ in range(len(grafo) - 1):
        for vertice in grafo:
            for vizinho, peso in grafo[vertice]:
                if distancias[vertice] + peso < distancias[vizinho]:
                    distancias[vizinho] = distancias[vertice] + peso

    # Verificando se há ciclos negativos
    for vertice in grafo:
        for vizinho, peso in grafo[vertice]:
            if distancias[vertice] + peso < distancias[vizinho]:
                raise ValueError("O grafo contém um ciclo negativo")

    return distancias

grafo = {
    'A': [('B', -1), ('C',  4)],
    'B': [('C',  3), ('D',  2), ('E',  2)],
    'C': [],
    'D': [('B',  1), ('C',  5)],
    'E': [('D', -3)]
}

distancias = bellman_ford(grafo, 'B')
print(distancias)
