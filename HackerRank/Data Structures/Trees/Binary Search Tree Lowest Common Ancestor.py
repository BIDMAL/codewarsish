class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def lca(root, a, b):
    node = root
    while node:
        if max(a, b) < node.info:
            node = node.left
        elif min(a, b) > node.info:
            node = node.right
        else:
            break
    return node
        
inp = ['6',
       '4 2 3 1 7 6',
       '1 7']

tree = BinarySearchTree()
t = int(inp[0])

arr = list(map(int, inp[1].split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, inp[2].split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
