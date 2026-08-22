"""
Módulo Árbol Binario de Búsqueda (BST).
Proyecto de freeCodeCamp: Learn Tree Traversal by Building a Binary Search Tree.
"""

class TreeNode:
    """Representa un nodo individual dentro del Árbol Binario de Búsqueda."""
    
    def __init__(self, key):
        """Inicializa el nodo con una clave y referencias nulas a sus hijos."""
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """Representa un Árbol Binario de Búsqueda (BST)."""
    
    def __init__(self):
        """Inicializa el BST con una raíz vacía (None)."""
        self.root = None

    def insert(self, key):
        """Inserta un nuevo valor manteniendo la propiedad del BST."""
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        """Función auxiliar recursiva para insertar un nodo en la posición correcta."""
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = TreeNode(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = TreeNode(key)
            else:
                self._insert_recursive(current_node.right, key)
        # Si key == current_node.key, no se permiten duplicados (se ignora)

    def search(self, key):
        """Busca un valor en el árbol. Retorna el nodo si existe o None en caso contrario."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        """Función auxiliar recursiva para buscar un nodo."""
        if current_node is None or current_node.key == key:
            return current_node
        
        if key < current_node.key:
            return self._search_recursive(current_node.left, key)
        return self._search_recursive(current_node.right, key)

    def delete(self, key):
        """Elimina un nodo del árbol manejando nodos hoja, con un hijo y con dos hijos."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current_node, key):
        """Función auxiliar recursiva para eliminar un nodo."""
        if current_node is None:
            return None
            
        if key < current_node.key:
            current_node.left = self._delete_recursive(current_node.left, key)
        elif key > current_node.key:
            current_node.right = self._delete_recursive(current_node.right, key)
        else:
            # Caso 1 y 2: Nodo hoja o nodo con un solo hijo
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
                
            # Caso 3: Nodo con dos hijos (reemplazar con el sucesor in-order del subárbol derecho)
            successor = self._find_min(current_node.right)
            current_node.key = successor.key
            current_node.right = self._delete_recursive(current_node.right, successor.key)
            
        return current_node

    def _find_min(self, node):
        """Encuentra el nodo con el valor mínimo a partir de un nodo dado."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """Realiza un recorrido in-order (Izquierda - Raíz - Derecha) y retorna una lista ordenada."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result):
        """Función auxiliar recursiva para el recorrido in-order."""
        if current_node:
            self._inorder_recursive(current_node.left, result)
            result.append(current_node.key)
            self._inorder_recursive(current_node.right, result)


if __name__ == '__main__':
    print("--- Árbol Binario de Búsqueda (BST) ---")
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    for val in values:
        bst.insert(val)
        
    print(f"Valores insertados: {values}")
    print(f"Recorrido In-Order (Ordenado): {bst.inorder_traversal()}")
    
    # Búsqueda
    search_val = 40
    node = bst.search(search_val)
    print(f"Buscar {search_val}: {'Encontrado' if node else 'No encontrado'}")
    
    # Eliminación de nodo hoja
    print("Eliminando nodo hoja (20)...")
    bst.delete(20)
    print(f"In-Order tras eliminar 20: {bst.inorder_traversal()}")
    
    # Eliminación de nodo con dos hijos
    print("Eliminando nodo con dos hijos (50 - raíz)...")
    bst.delete(50)
    print(f"In-Order tras eliminar 50: {bst.inorder_traversal()}")