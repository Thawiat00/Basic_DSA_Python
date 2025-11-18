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

def insertNodeAtPosition(head, newNode, position):
    # แทรกที่ตำแหน่งแรก
    if position == 1:
        newNode.next = head
        return newNode
    
    # หาตำแหน่งที่จะแทรก
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next
    
    # แทรก node
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

# ทดสอบ
newNode = Node(99)
node1 = insertNodeAtPosition(node1, newNode, 2)  # แทรกที่ตำแหน่งที่ 2

traverseAndPrint(node1)