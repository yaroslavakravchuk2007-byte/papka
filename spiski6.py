class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def top(self):
        if not self.items:
            return None
        return self.items[-1]

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()
    stack = Stack()

while True:
    print("\nВыберите действие:")
    print("1 - Добавить элемент (push)")
    print("2 - Удалить элемент (pop)")
    print("3 - Посмотреть верхний элемент (top)")
    print("4 - Показать все элементы стека")
    print("0 - Выход")
    
    choice = input("Введите номер действия: ")
    
    if choice == "1":
        value = input("Введите значение для добавления: ")
        stack.push(value)
        print(f"Элемент '{value}' добавлен в стек.")
    
    if choice == "2":
        popped = stack.pop()
        if popped is None:
            print("Стек пуст.")
        else:
            print(f"Удален элемент: {popped}")
    
    if choice == "3":
        top_item = stack.top()
        if top_item is None:
            print("Стек пуст.")
        else:
            print(f"Верхний элемент: {top_item}")
    
    if choice == "4":
        print("Текущий стек:", stack.items)
    
    if choice == "0":
        print("Выход из программы.")
        break
    
    if choice not in ["0", "1", "2", "3", "4"]:
        print("Неверный выбор, попробуйте снова.")

    # спасибо чатику гпт за помощь в реализации кодадля ввода и вывода данных