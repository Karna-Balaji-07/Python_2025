# implementing stack in linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None
    
    def push(self,data):
        new_node = Node(data)
        if not new_node:
            print("Stack overflow")
            return 
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            temp = self.head
            self.head = self.head.next
            del temp

    def peek(self):
        if self.isEmpty():
            return self.head.data
        else:
            print("Stack underflow")
            return float('-inf')
    

# Creating a stack
st = Stack()

# Push elements onto the stack
st.push(11)
st.push(22)
st.push(33)
st.push(44)

# Print top element of the stack
print("Top element is", st.peek())

# removing two elemements from the top
print("Removing two elements...");
st.pop()
st.pop()

# Print top element of the stack
print("Top element is", st.peek())