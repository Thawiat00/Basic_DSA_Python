# สร้าง Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# สร้าง nodes
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)

# เชื่อมโยง nodes
node1.next = node2
node2.next = node3

print(node1.data)        # 7
print(node1.next.data)   # 11
print(node2.data)       # 11
print(node2.next.data)  #3
print(node3.data)       #3
#print(node3.next.data) 