# สร้าง Queue
queue = []

# Enqueue (เพิ่มคนเข้าคิว)
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue:", queue)

# Peek (ดูคนหน้าสุด)
frontElement = queue[0]
print("Peek:", frontElement)

# Dequeue (เอาคนหน้าสุดออก)
poppedElement = queue.pop(0)
print("Dequeue:", poppedElement)
print("Queue หลัง Dequeue:", queue)

# ตรวจสอบว่าง
isEmpty = not bool(queue)
print("Queue ว่างไหม:", isEmpty)

# นับจำนวน
print("ขนาด:", len(queue))