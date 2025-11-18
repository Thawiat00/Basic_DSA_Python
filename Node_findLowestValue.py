# สร้าง Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

# ทดสอบ
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    
    return minValue

# ทดสอบ
print("ค่าต่ำสุด:", findLowestValue(node1))  # Output: 2