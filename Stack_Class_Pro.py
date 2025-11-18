class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        """เพิ่มสมาชิกเข้า stack"""
        self.stack.append(element)
    
    def pop(self):
        """เอาสมาชิกบนสุดออก"""
        if self.isEmpty():
            return "Stack ว่าง"
        return self.stack.pop()
    
    def peek(self):
        """ดูสมาชิกบนสุด"""
        if self.isEmpty():
            return "Stack ว่าง"
        return self.stack[-1]
    
    def isEmpty(self):
        """ตรวจสอบว่า stack ว่างไหม"""
        return len(self.stack) == 0
    
    def size(self):
        """นับจำนวนสมาชิก"""
        return len(self.stack)

# ทดลองใช้
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')
myStack.push('C')

print("Stack:", myStack.stack)
print("Pop:", myStack.pop())
print("Stack หลัง Pop:", myStack.stack)
print("Peek:", myStack.peek())
print("ว่างไหม:", myStack.isEmpty())
print("ขนาด:", myStack.size())