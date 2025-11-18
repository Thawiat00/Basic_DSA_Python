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

# ลองสร้าง Stack เก็บประวัติการเรียกดูหน้าเว็บ
browser_history = Stack()
browser_history.push('google.com')
browser_history.push('facebook.com')
browser_history.push('youtube.com')

print("หน้าปัจจุบัน:", browser_history.peek())
print("กดปุ่ม Back:", browser_history.pop())
print("หน้าปัจจุบัน:", browser_history.peek())