class TreeNode:
    def __init__(self, key):
        self.key = key         # La chiave del nodo
        self.left = None       # Riferimento al figlio sinistro
        self.right = None      # Riferimento al figlio destro

    def __str__(self):
        return str(self.key)   # Metodo per restituire la rappresentazione in stringa della chiave del nodo


class BinarySearchTree:
    def __init__(self):
        self.root = None       # L'albero inizia senza nodi, quindi la radice è None

    
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)   # Se il nodo corrente è None, crea un nuovo nodo con la chiave

        if key < node.key:
            node.left = self._insert(node.left, key)  # Inserisce ricorsivamente nella sottoalbero sinistro
        elif key > node.key:
            node.right = self._insert(node.right, key)  # Inserisce ricorsivamente nella sottoalbero destro
        return node  # Restituisce il nodo corrente

    def insert(self, key):
        self.root = self._insert(self.root, key)  # Inserisce un nodo a partire dalla radice

    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node  # Restituisce il nodo se trovato o None se non esiste
        if key < node.key:
            return self._search(node.left, key)  # Cerca ricorsivamente nel sottoalbero sinistro
        return self._search(node.right, key)  # Cerca ricorsivamente nel sottoalbero destro
    
    def search(self, key):
        return self._search(self.root, key)  # Cerca un nodo a partire dalla radice


    def _delete(self, node, key):
        if node is None:
            return node  # Se il nodo è None, ritorna None
        if key < node.key:
            node.left = self._delete(node.left, key)  # Elimina ricorsivamente nel sottoalbero sinistro
        elif key > node.key:
            node.right = self._delete(node.right, key)  # Elimina ricorsivamente nel sottoalbero destro
        else:
            # Nodo trovato: gestisce i casi in cui il nodo ha uno o nessun figlio
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Nodo con due figli: trova il successore (minimo del sottoalbero destro)
            node.key = self._min_value(node.right)
            # Elimina il successore nel sottoalbero destro
            node.right = self._delete(node.right, node.key)
        return node  # Restituisce il nodo corrente (possibilmente aggiornato)

    def delete(self, key):
        self.root = self._delete(self.root, key)  # Elimina un nodo a partire dalla radice

    def _min_value(self, node):
        while node.left is not None:
            node = node.left  # Trova il nodo con la chiave minima (più a sinistra)
        return node.key  # Restituisce la chiave del nodo minimo

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)  # Visita ricorsivamente il sottoalbero sinistro
            result.append(node.key)  # Aggiunge la chiave del nodo corrente alla lista dei risultati
            self._inorder_traversal(node.right, result)  # Visita ricorsivamente il sottoalbero destro
    
    def inorder_traversal(self):
        result = []  # Lista per memorizzare le chiavi in ordine
        self._inorder_traversal(self.root, result)  # Avvia la visita in ordine a partire dalla radice
        return result  # Restituisce la lista delle chiavi in ordine

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)  # Inserisce i nodi nell'albero

print('Search for 80:', bst.search(80))  # Cerca il nodo con chiave 80

print("Inorder traversal:", bst.inorder_traversal())  # Stampa la visita in ordine dei nodi

bst.delete(40)  # Elimina il nodo con chiave 40

print("Search for 40:", bst.search(40))  # Cerca il nodo con chiave 40 (dovrebbe essere None)
print('Inorder traversal after deleting 40:', bst.inorder_traversal())  # Stampa la visita in ordine dei nodi dopo la cancellazione
