def BFS(raiz):
    if not raiz: return []
    respuesta = [raiz]
    cola = [raiz]
    nivel = 1
    while cola:
        for _ in range(len(cola)):
            nodoActual = cola.pop(0)
            print(nodoActual.valor)
            respuesta.append(nodoActual)
            for hijo in nodoActual.hijos:
                cola.append(hijo)
        nivel += 1
    print(f"Cantidad de niveles del árbol: {nivel}")
    return respuesta

