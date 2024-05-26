# Definiamo un grafo come un dizionario. Le chiavi sono i nodi e i valori sono liste di tuple,
# dove ogni tupla rappresenta un nodo adiacente e la distanza da quel nodo.
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    # Inizializziamo l'insieme dei nodi non visitati come una lista di tutti i nodi nel grafo.
    unvisited = list(graph)
    
    # Inizializziamo il dizionario delle distanze. La distanza iniziale per il nodo di partenza è 0,
    # per tutti gli altri nodi è impostata a infinito.
    distances = {node: 0 if node == start else float('inf') for node in graph}
    
    # Inizializziamo il dizionario dei percorsi. Ogni nodo ha una lista vuota di percorsi inizialmente.
    paths = {node: [] for node in graph}
    # Aggiungiamo il nodo di partenza al percorso iniziale di se stesso.
    paths[start].append(start)
    
    # Continua finché ci sono nodi non visitati.
    while unvisited:
        # Troviamo il nodo non visitato con la distanza minima.
        current = min(unvisited, key=distances.get)
        
        # Per ogni nodo adiacente e la distanza da esso nel grafo corrente:
        for node, distance in graph[current]:
            # Se trovare un percorso più breve al nodo adiacente attraverso il nodo corrente:
            if distance + distances[current] < distances[node]:
                # Aggiorniamo la distanza minima al nodo adiacente.
                distances[node] = distance + distances[current]
                
                # Aggiorniamo il percorso verso il nodo adiacente.
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                
                # Aggiungiamo il nodo adiacente alla fine del percorso.
                paths[node].append(node)
        
        # Rimuoviamo il nodo corrente dall'insieme dei nodi non visitati.
        unvisited.remove(current)

    # Utilizziamo la sintassi ternaria per assegnare 'targets_to_print'.
    # Se 'target' è truthy, assegniamo '[target]', altrimenti assegniamo 'graph'.
    targets_to_print = [target] if target else graph.keys()
    
    # Stampiamo le distanze e i percorsi per ciascun nodo in 'targets_to_print'.
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    # Restituiamo le distanze e i percorsi trovati.
    return distances, paths

# Chiamiamo la funzione 'shortest_path' con il grafo 'my_graph' e il nodo di partenza 'A'.
shortest_path(my_graph, 'A')
