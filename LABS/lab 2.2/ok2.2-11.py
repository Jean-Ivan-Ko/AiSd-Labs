class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def balance(self, node):
        balance_factor = self.get_balance(node)
        if balance_factor > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance_factor < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node
        self.update_height(node)
        return self.balance(node)

    def delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)
        self.update_height(node)
        return self.balance(node)

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def exists(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.exists(node.left, key)
        else:
            return self.exists(node.right, key)

    def next(self, node, key):
        successor = None
        while node:
            if node.key > key:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor.key if successor else None

    def prev(self, node, key):
        predecessor = None
        while node:
            if node.key < key:
                predecessor = node
                node = node.right
            else:
                node = node.left
        return predecessor.key if predecessor else None


with open('input.txt', 'r') as file:
    commands = file.readlines()


avl_tree = AVLTree()
root = None


output = []

for command in commands:
    parts = command.split()
    operation = parts[0]
    x = int(parts[1])

    if operation == 'insert':
        root = avl_tree.insert(root, x)

    elif operation == 'delete':
        root = avl_tree.delete(root, x)

    elif operation == 'exists':
        if avl_tree.exists(root, x):
            output.append("true")
        else:
            output.append("false")

    elif operation == 'next':
        result = avl_tree.next(root, x)
        if result is not None:
            output.append(str(result))
        else:
            output.append("none")

    elif operation == 'prev':
        result = avl_tree.prev(root, x)
        if result is not None:
            output.append(str(result))
        else:
            output.append("none")


with open('output.txt', 'w') as file:
    file.write("\n".join(output) + "\n")