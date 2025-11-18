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

# ลองจำลองคิวที่ร้านกาแฟ
coffee_queue = Queue()

# ลูกค้าเข้าคิว
coffee_queue.enqueue('คุณสมชาย')
coffee_queue.enqueue('คุณสมหญิง')
coffee_queue.enqueue('คุณสมศรี')

print("คิวทั้งหมด:", coffee_queue.queue)
print("กำลังทำกาแฟให้:", coffee_queue.dequeue())
print("ถัดไปคือ:", coffee_queue.peek())
print("คิวที่เหลือ:", coffee_queue.queue)