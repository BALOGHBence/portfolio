import os
from anytree import Node, RenderTree

def build_tree(root):
    root_node = Node(root)
    nodes = {root: root_node}
    for dirpath, dirnames, filenames in os.walk(root):
        for dirname in dirnames:
            node = Node(dirname, parent=nodes[dirpath])
            nodes[os.path.join(dirpath, dirname)] = node
        for filename in filenames:
            if 'printtree.py' in filename:
                continue
            Node(filename, parent=nodes[dirpath])
    return root_node

def print_tree(root):
    root_node = build_tree(root)
    for pre, fill, node in RenderTree(root_node):
        print(f"{pre}{node.name}")

# Usage
root_directory = r"D:\Projects\portfolio"
print_tree(root_directory)
