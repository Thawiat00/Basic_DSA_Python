# สร้าง Stack
stack = []

# Push (เพิ่มเข้า stack)
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack:", stack)

# Peek (ดูตัวบนสุดโดยไม่เอาออก)
topElement = stack[-1]
print("Peek:", topElement)

# Pop (เอาตัวบนสุดออก)
poppedElement = stack.pop()
print("Pop:", poppedElement)
print("Stack หลัง Pop:", stack)

# ตรวจสอบว่าง
isEmpty = not bool(stack)
print("Stack ว่างไหม:", isEmpty)

# นับจำนวน
print("ขนาด:", len(stack))