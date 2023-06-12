import heapq

def dijkstra(grafo, v1):
    # inicializando as distancias para todos os vertices com infinito, menos o vertice inicial
    distancias = {vertice : [float('inf'), []] for vertice in grafo}
    distancias[v1] = [0, [v1]]
    
    # heap onde está a tupla (distancia, vertice)
    vertdist = [(0, v1)]
    
    while vertdist:
        distanciaAtual, verticeAtual = heapq.heappop(vertdist)
        
        
        if distanciaAtual > distancias[verticeAtual][0]:
            continue
    
        for vizinho, peso in grafo[verticeAtual]:
            distancia = distanciaAtual + peso

            
            if distancia < distancias[vizinho][0]:
                distancias[vizinho] = [distancia, distancias[verticeAtual][1] + [vizinho]]
                heapq.heappush(vertdist, (distancia, vizinho))
    return distancias



graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 4), ('B', 1), ('D', 2)],
    'D': [('B', 4), ('C', 2)]
}

# Executa o algoritmo de Dijkstra a partir do vértice A
distances = dijkstra(graph, 'A')

# Imprime o resultado
for vertex, (distance, path) in distances.items():
    print(f"Menor caminho de A até {vertex}: {path}, com distância {distance}")