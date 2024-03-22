class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top_node = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        if self.top_node is None:
            self.top_node = new_node
        else:
            new_node.next = self.top_node
            self.top_node = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.size -= 1
            return popped_item

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.top_node.data

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


stack = LinkedStack()
stack.push(4)
stack.push(5)
stack.push(7)

print("Tope de la pila:", stack.top())

print("Elemento extraído:", stack.pop())
print("Elemento extraído:", stack.pop())

print("¿La pila está vacía?", stack.is_empty())
print("Tamaño de la pila:", len(stack))
