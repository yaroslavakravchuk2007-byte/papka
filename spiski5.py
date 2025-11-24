class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new = DNode(data)
        if not self.head:
            self.head = self.tail = new
            return
        self.tail.next = new
        new.prev = self.tail
        self.tail = new

def compute_pairs_doubly(lst: DoublyLinkedList):
    left = lst.head
    right = lst.tail
    result = []

    while left and right and left != right and left.prev != right:
        result.append(left.data - right.data)
        left = left.next
        right = right.prev

    return result
n = int(input("Введите количество элементов списка: "))
dll = DoublyLinkedList()

print("Введите элементы списка:")
for _ in range(n):
    value = int(input())
    dll.append(value)


result = compute_pairs_doubly(dll)
print("Результат вычисления пар:", result)