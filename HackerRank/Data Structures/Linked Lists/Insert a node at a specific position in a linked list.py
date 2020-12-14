inp = ['5',
       '141',
       '302',
       '164',
       '530',
       '474',
       '1',
       '2']

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next

def insertNodeAtPosition(head, data, position):
    ln = SinglyLinkedListNode(data)
    cp = 0
    if (not head) or (not position):
        return ln
    else:
        cur = head
        while cur.next and cp < position-1:
            cp += 1
            cur = cur.next
        ln.next = cur.next
        cur.next = ln        
    return head

llist_count = int(inp[0])
llist = SinglyLinkedList()
for i in range(llist_count):
    llist_item = int(inp[1+i])
    llist.insert_node(llist_item)
data = int(inp[llist_count+1])
position = int(inp[llist_count+2])
llist_head = insertNodeAtPosition(llist.head, data, position)
print_singly_linked_list(llist_head)
