class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new


def search_in_singly(lst: SinglyLinkedList, target):
    cur = lst.head
    while cur:
        if cur.data == target:
            return True
        cur = cur.next
    return False


n = int(input())
values = list(map(int, input().split()))
target = int(input())

lst = SinglyLinkedList()
for v in values:
    lst.append(v)

result = search_in_singly(lst, target)

print(str(result).lower())
