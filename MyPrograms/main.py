class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def pop(self):
        # Удаляет первый элемент (голову)
        if self.head:
            self.head = self.head.next
        else:
            print("List is empty.")

    def remove_by_value(self, value):
        # Удаляет первый узел с указанным значением
        current = self.head
        prev = None

        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next  # Если удаляем голову
                return
            prev = current
            current = current.next

        print(f"Value {value} not found in the list.")

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


# Использование
llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)

# Удаление элемента со значением
llist.remove_by_value(20)

llist.print_list()
