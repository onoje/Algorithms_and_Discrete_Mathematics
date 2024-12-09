class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def _init_(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key

# Programın test edilmesi
bst = BinarySearchTree()
keys = [20, 8, 22, 4, 12, 10, 14]  # Örnek veri
for key in keys:
    bst.insert(key)

print("Minimum değer:", bst.find_min())
print("Maximum değer:", bst.find_max())