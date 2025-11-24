def print_reverse_doubly(lst: DoublyLinkedList):
    cur = lst.tail
    while cur:
        print(cur.data, end=" ")
        cur = cur.prev
    print()
