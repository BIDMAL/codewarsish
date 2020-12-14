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

inp = ['6',
       '1 2 5 3 6 4']

#def mergeView(resr, resl):
#    ret = resl
#    for key, value in resr.items():
#        if key not in ret.keys():
#            ret[key] = value
#        else:
#            ret[key].extend(value)
#    return ret
#    
#
#def levelOrder(root):
#    def getLevel(node, lvl):
#        res = {}
#        if node :
#            resr = getLevel(node.right, lvl+1)
#            resl = getLevel(node.left, lvl+1)
#            res = mergeView(resr, resl)
#            res[lvl] = [node.info]
#        return res
#    view = getLevel(root, 0)
#    lvls = sorted(view)
#    for lvl in lvls:
#        print(*view[lvl], end=' ')

def levelOrder(root):
    queue = []
    queue.append(root)
    while(len(queue)>0):
        node = queue.pop(0)
        print(node.info, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

tree = BinarySearchTree()
t = int(inp[0])

arr = list(map(int, inp[1].split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)