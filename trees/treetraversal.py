class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
# Create binary tree
    #       1
    #      /  \
    #    2     3
    #   / \     \
    #  4   5     6
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)




#dfs:firstly goes the deepest node.


#in-order: left-root-right. if applied to bst, it returns elements in sorted order

res=[]
def inorder(node,res):
    if node is None:
        return
    inorder(node.left,res)
    res.append(node.data)
    inorder(node.right,res)
    
inorder(root,res)


#pre-order: first visit node itself, then left, then right.

res=[]
def preorder(node,res):
    if node is None:
        return
    res.append(node.data)
    inorder(node.left,res)
    inorder(node.right,res)

#post-order traversal: first finish sutrees of each node, then node itself.

res=[]
def postorder(node,res):
    if node is None:
        return
    postorder(node.left,res)
    postorder(node.right,res)
    res.append(node.data)

#bfs: it explores the grap level by level.


def breadthfirst(node):
    res=[]
    queue=[node]
    while queue:
        node=queue.pop(0)
        res.append(node.data)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res

res=breadthfirst(root)
print(res)

