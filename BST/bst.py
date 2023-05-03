class _Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None



class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def add(self, key, value):
        node = _Node(key, value)
        if self._root is None:
            self._root = node
            self._size += 1
            return

        x = self._root
        y=None
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if node.key < y.key:
            y.left = node
        else:
            y.right = node
        self._size += 1

    def search(self, key):
        node = self._search(key, self._root)
        return node.value if node else False

    def _search(self, key, node):
        #recursively search for a node with the given key
        if node is None:
            return False
        if key < node.key:
            return self._search(key, node.left)
        elif key > node.key:
            return self._search(key, node.right)
        else:
            return node

    def inorder_walk(self):
        # Returns a list of the keys of the nodes in the binary search tree
        walk = list()
        self._inorder_walk(self._root,  walk)
        return walk

    def _inorder_walk(self, node, walk):
        if node is None:
            return
        self._inorder_walk(node.left, walk)
        walk.append(node.key)
        self._inorder_walk(node.right, walk)

        return walk

    def postorder_walk(self):
        walk = list()
        self._postorder_walk(self._root,  walk)
        return walk

    def _postorder_walk(self, node, walk):
        if node is None:
            return
        self._postorder_walk(node.left, walk)
        self._postorder_walk(node.right, walk)
        walk.append(node.key)

        return walk

    def preorder_walk(self):
        walk = list()
        self._preorder_walk(self._root,  walk)
        return walk

    def _preorder_walk(self, node, walk):
        if node is None:
            return
        walk.append(node.key)
        self._preorder_walk(node.left, walk)
        self._preorder_walk(node.right, walk)

        return walk

    def _smallest(self, node):
        if node.left is None:
            return node
        return self._smallest(node.left)

    def smallest(self):
        node = self._smallest(self._root)
        return (node.key, node.value)

    def _largest(self, node):
        if node.right is None:
            return node
        return self._largest(node.right)

    def largest(self):
        node = self._largest(self._root)
        return (node.key, node.value)

    def size(self):
        return self._size

bst = BinarySearchTree()

# Add some nodes
bst.add(5, "value for five")
bst.add(3, "value for three")
bst.add(7, "value for seven")
bst.add(1, "value for one")
bst.add(4, "value for four")
bst.add(6, "value for six")
bst.add(8, "value for eight")

# Print the inorder, preorder, and postorder walks
print("Inorder walk:", bst.inorder_walk())
print("Preorder walk:", bst.preorder_walk())
print("Postorder walk:", bst.postorder_walk())

# Print the smallest and largest nodes
print("Smallest:", bst.smallest())
print("Largest:", bst.largest())

# Remove a node
bst.remove(3)

# Print the inorder walk again to see that the node was removed
print("Inorder walk after removing 3:", bst.inorder_walk())

# Get the value of a node
value = bst.search(7)
print("Value of 7:", value)

# Get the size of the tree
size = bst.size()
print("Size of tree:", size)
