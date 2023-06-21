def preparar_matriz(matriz): # Llena de infinitos la matriz
    for i in range (0, len(matriz)):
        for j in range (0, len(matriz)):
            if i != j and matriz[i][j] == 0:
                matriz[i][j] = float("inf")

def floyd(matriz): # Antes de ejecutar esta funcion, ejeccutar "preparar_matriz"
    for k in range (0, len(matriz)):
        for i in range (0, len(matriz)):
            for j in range (0, len(matriz)):
                if matriz[i][j] > matriz[i][k] + matriz[k][j]:
                    matriz[i][j] = matriz[i][k] + matriz[k][j]
    return matriz

def distancia_menor(resultados, visitados):
    dist = float('inf')
    nodo = None
    for r in resultados:
        if resultados[r]["Distancia"] < dist and r not in visitados:
            dist = resultados[r]["Distancia"]
            nodo = r
    return nodo

def dijkstra(grafo, inicio):
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
    
def recontruir_camino(resultados, inicio, fin):
    camino = []
    actual = fin
    while actual != inicio:
        camino = [actual] + camino
        actual = resultados[actual]["Anterior"]
    camino = [inicio] + camino
    return camino  

def encontrar_arista_menor_prim (grafo, visitados):
    nodo_inicio = ""
    nodo_fin = ""
    menor_peso = float("inf")
    if len(visitados) == 0:
        for inicio in grafo:
            for fin in grafo[inicio]:
                if grafo[inicio][fin] < menor_peso:
                    menor_peso = grafo[inicio][fin]
                    nodo_inicio = inicio
                    nodo_fin = fin
    else:
        for inicio in visitados:
            for fin in grafo[inicio]:
                if grafo[inicio][fin] < menor_peso and fin not in visitados:
                    menor_peso = grafo[inicio][fin]
                    nodo_inicio = inicio
                    nodo_fin = fin
                    
    return nodo_inicio, nodo_fin, menor_peso
    
def prim (grafo):
    mst = {}
    visitados = []
    while len(visitados) < len(grafo):
        inicio, fin, peso = encontrar_arista_menor_prim(grafo, visitados)
        print(inicio, fin, peso)
        if inicio not in visitados:
            visitados.append(inicio)
        if fin not in visitados:
            visitados.append(fin)
        if inicio in mst:
            mst[inicio][fin] = peso
        else:
            mst[inicio] = {fin: peso}
    return mst


from operator import itemgetter
def kruskal (grafo):
    arm = {}
    arboles = []
    aristas = 0
    lista_ordenada = ordenar_lista(grafo)
    while aristas != len(grafo)-1:
        inicio, fin, peso = lista_ordenada.pop(0)
        agregar = anadir_nodos(arboles, inicio, fin)
        if agregar == True:
            print(inicio, fin, peso) # No es necesario, sirve para ver el orden
            aristas += 1
            if inicio not in arm:
                arm[inicio] = {}
            arm[inicio][fin] = peso
    return arm

def ordenar_lista (grafo):
    resultado = []
    for i in grafo:
        for f in grafo[i]:
            resultado.append((i, f, grafo[i][f]))
            resultado.sort(key=itemgetter(2))
    return resultado

def anadir_nodos(arboles, inicio, fin):
    indice_inicio = indice_fin = None
    for i in range(0, len(arboles)):
        if inicio in arboles[i]:
            indice_inicio = i
        if fin in arboles[i]:
            indice_fin = i

    if indice_inicio == None and indice_fin != None:
        arboles[indice_fin].append(inicio)
        return True
    elif indice_inicio != None and indice_fin == None:
        arboles[indice_inicio].append(fin)
        return True
    elif indice_inicio == None and indice_fin == None:
        arboles.append([inicio, fin])
        return True
    elif indice_inicio != None and indice_fin != None and indice_inicio != indice_fin:
        arboles.append(arboles[indice_inicio]+arboles[indice_fin])
        quitar_inicio = arboles[indice_inicio]
        quitar_fin = arboles[indice_fin]
        arboles.remove(quitar_inicio)
        arboles.remove(quitar_fin)
        return True

