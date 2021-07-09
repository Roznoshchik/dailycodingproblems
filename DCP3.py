"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes 
the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'


# Personal notes # 
This was a bitch. I'm surprised they rated this as a medium level problem.
Guess I've been living in a whole different universe of coding, if that's
medium to some people. Felt a bit next level to me. Thinking in terms of 
tree traversal is not at all intuitive and took my brain forever to make sense of things.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    string = str(node.val)
    if node.left and node.left.val:
        string += " "
        string += serialize(node.left) 
    else:
        string += " NULL"
    if node.right and node.right.val:
        string += " "
        string += serialize(node.right)
    else:
        string += " NULL"
                
    return string


def deserialize(str):
    arr = str.split(' ')
    root = Node(arr[0])
    arr.pop(0)
    record = {root:{"parent":None}}
    recreate_tree(root, arr, record)
    return root

def recreate_tree(node, arr, record):
    if len(arr) == 0:
        return
    if node.left in record and node.right in record:
        recreate_tree(record[node]["parent"], arr, record)
    elif node.left in record:
        if arr[0] != "NULL":
            node.right = Node(arr[0])
            record[node.right] = {"parent":node, "visited":True}
            arr.pop(0)
            recreate_tree(node.right, arr, record)
        else:
            node.right = Node(None)
            record[node.right] = {"parent":node, "visited":True}
            arr.pop(0)
            recreate_tree(record[node]['parent'], arr, record)
    else:
        if arr[0] != "NULL":
            node.left = Node(arr[0])
            record[node.left] = {"parent":node, "visited":True}
            arr.pop(0)
            recreate_tree(node.left, arr, record)
        else:
            node.left = Node(None)
            record[node.left] = {"parent":node, "visited":True}
            arr.pop(0)
            recreate_tree(node, arr, record)

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'