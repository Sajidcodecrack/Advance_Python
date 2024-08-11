import random
from graphviz import Digraph

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root

def inorder_traversal(root, graph):
    if root:
        inorder_traversal(root.left, graph)
        graph.node(str(root.value))
        if root.left:
            graph.edge(str(root.left.value), str(root.value))
        if root.right:
            graph.edge(str(root.value), str(root.right.value))
        inorder_traversal(root.right, graph)

def generate_random_tree(size):
    root = None
    for _ in range(size):
        value = random.randint(1, 100)
        root = insert(root, value)
    return root

# Generate a random binary tree with 12 nodes
tree_root = generate_random_tree(12)

# Create a graph to visualize the inorder traversal
graph = Digraph('InorderTraversal', node_attr={'shape': 'circle'})
inorder_traversal(tree_root, graph)

# Save the graph as a PNG file
graph.render(filename='inorder_traversal', format='png', cleanup=True)

print("Inorder Traversal Graph generated and saved as 'inorder_traversal.png'")
