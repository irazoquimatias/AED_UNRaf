def dijkstra(grafo, inicio):  # Grafo debe ser un diccionario!!
    actual = inicio
    visitados = []
    resultados = {}
    for g in grafo:
        if g == inicio:
            resultados[g] = {"Distancia": 0, "Anterior": None}
        else:
            resultados[g] = {"Distancia": float("inf"), "Anterior": None}
    while actual != None:
        visitados.append(actual)
        for g in grafo[actual]:
            if resultados[g]["Distancia"] > resultados[actual]["Distancia"] + grafo[actual][g]:
                resultados[g]["Distancia"] = resultados[actual]["Distancia"] + grafo[actual][g]
                resultados[g]["Anterior"] = actual
    actual = distancia_menor(resultados, visitados)
    return resultados

def distancia_menor(resultados, visitados):
    dist = float('inf')
    nodo = None
    for r in resultados:
        if resultados[r]["Distancia"] < dist and r not in visitados:
            dist = resultados[r]["Distancia"]
            nodo = r
    return nodo

def recontruir_camino(resultados, inicio, fin):
    camino = []
    actual = fin
    while actual != inicio:
        camino = [actual] + camino
        actual = resultados[actual]["Anterior"]
    camino = [inicio] + camino
    return camino

def preparar_matriz(matriz):
    for i in range (0, len(matriz)):
        for j in range (0, len(matriz)):
            if i != j and matriz[i][j] == 0:
            matriz[i][j] = float("inf")
    return matriz
    
def floyd(matriz):
    for k in range (0, len(matriz)):
        for i in range (0, len(matriz)):
            for j in range (0, len(matriz)):
                if matriz[i][j] > matriz[i][k] + matriz[k][j]:
                    matriz[i][j] = matriz[i][k] + matriz[k][j]
    return matriz
