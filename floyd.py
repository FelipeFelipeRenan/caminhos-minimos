def floyd_warshall(grafo):
    n = len(grafo)
    
    # inicializa a matriz de distâncias com os valores das arestas existentes
    distancias = [[float('inf')]*n for _ in range(n)]
    
    for u in range(n):
        distancias[u][u] = 0
        for v, w in grafo[u]:
            distancias[u][v] = w
    
    # executa o algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancias[i][k] != float('inf') and distancias[k][j] != float('inf'):
                    distancias[i][j] = min(distancias[i][j], distancias[i][k]+distancias[k][j])
                    
    return distancias


# grafo representado por uma lista de listas, onde cada indice da lista
# é um vertice do grafo
grafo = [
    [(1, 3), (3, 5)],  
    [(2, 2)],          
    [(3, 4)],           
    []                 
]

dist = floyd_warshall(grafo)

for linha in dist:
    print(linha)