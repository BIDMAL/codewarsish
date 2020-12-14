inp = ['5',
       '141',
       '302',
       '164',
       '530',
       '474']

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next

def insertNodeAtTail(head, data):
    ln = SinglyLinkedListNode(data)
    if not head:
        return ln
    else:
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = ln
    return head

llist_count = int(inp[0])
llist = SinglyLinkedList()
for i in range(llist_count):
    llist_item = int(inp[1+i])
    llist_head = insertNodeAtTail(llist.head, llist_item)
    llist.head = llist_head
print_singly_linked_list(llist.head)
