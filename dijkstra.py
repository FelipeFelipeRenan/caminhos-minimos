import heapq

def dijkstra(grafo, v1):
    # inicializando as distancias para todos os vertices com infinito, menos o vertice inicial
    distancias = {vertice : [float('inf'), []] for vertice in grafo}
    distancias[v1] = [0, [v1]]
    
    # heap onde está a tupla (distancia, vertice)
    vertdist = [(0, v1)]
    
    # enquanto a heap nao estiver vazia
    while vertdist:
        # o vertice com menor distancia é retirado da heap
        distanciaAtual, verticeAtual = heapq.heappop(vertdist)
        
        # caso a distancia da iteração atual for maior que a presente no vetor de distancia
        # segue para o proximo vertice
        if distanciaAtual > distancias[verticeAtual][0]:
            continue
        
        # iteração emtre todos os vizinhos do vertice atual e calcula
        # suas respectivas distancias
        for vizinho, peso in grafo[verticeAtual]:
            distancia = distanciaAtual + peso

            
            if distancia < distancias[vizinho][0]:
                distancias[vizinho] = [distancia, distancias[verticeAtual][1] + [vizinho]]
                heapq.heappush(vertdist, (distancia, vizinho))
    
    # retorna um dicionario com as distancias
    return distancias


# lista de adjacencias representada por um dicionario
# contendo os vertices como chave uma lista composta por tuplas
# representado os seus respectivos vizinhos e suas distancias para
# o vertice na chava
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 4), ('B', 1), ('D', 2)],
    'D': [('B', 4), ('C', 2)]
}

# Executa o algoritmo de Dijkstra a partir do vértice A
distancias = dijkstra(graph, 'A')

# Imprime o resultado
for vertice, (distancia, caminho) in distancias.items():
    print(f"Menor caminho de A até {vertice}: {caminho}, com distância {distancia}")