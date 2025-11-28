class Node:
    def __init__(self,x):
        self.data=x
        self.children=[]
def addchild(parent,child):
    parent.children.append(child)

    #print parents of each node
def printparent(node,parent):
    if parent is None:
        print(f"{node.data} is Null")
    else:
        print(f"{node.data}'s parent is {parent.data}")
    for child in node.children:
        (printparent(child,node))

def printdegree(node,parent):
    degree=len(node.children)
    if parent is not None:
        degree+=1
    print(f"{node.data} -> {degree}")
    for child in node.children:
        printdegree(child,node)

def degree(node,parent):
    if node.children:
        print(f"{node.data} has degree of {len(node.children)}")
    for child in node.children:
        degree(child,node)
root=Node(1)

n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)


addchild(root,n2)
addchild(root,n3)
addchild(n2,n4)
addchild(n2,n5)

printparent(root,None)
printdegree(root,None)
degree(root,None)
