class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        """เพิ่มคนเข้าคิว (ท้ายสุด)"""
        self.queue.append(element)
    
    def dequeue(self):
        """เอาคนหน้าสุดออก"""
        if self.isEmpty():
            return "Queue ว่าง"
        return self.queue.pop(0)
    
    def peek(self):
        """ดูคนหน้าสุด"""
        if self.isEmpty():
            return "Queue ว่าง"
        return self.queue[0]
    
    def isEmpty(self):
        """ตรวจสอบว่า queue ว่างไหม"""
        return len(self.queue) == 0
    
    def size(self):
        """นับจำนวนคน"""
        return len(self.queue)

# ทดลองใช้
myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue:", myQueue.queue)
print("Peek:", myQueue.peek())
print("Dequeue:", myQueue.dequeue())
print("Queue หลัง Dequeue:", myQueue.queue)
print("ว่างไหม:", myQueue.isEmpty())
print("ขนาด:", myQueue.size())