inp = ['8',
       '20',
       '6',
       '2',
       '19',
       '7',
       '4',
       '15',
       '9',
       '3']

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

def reverse(head):
    head2 = None
    while head:        
        ln = SinglyLinkedListNode(head.data)
        nx = head2
        head2 = ln
        head2.next = nx
        head = head.next
    return head2 

llist_count = int(inp[0])
llist = SinglyLinkedList()
for i in range(llist_count):
    llist_item = int(inp[1+i])
    llist.insert_node(llist_item)
position = int(inp[llist_count+1])
llist1 = reverse(llist.head)
print_singly_linked_list(llist1)
