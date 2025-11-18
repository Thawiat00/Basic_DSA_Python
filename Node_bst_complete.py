class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    """เพิ่ม node ใหม่เข้า BST"""
    if node is None:
        return TreeNode(data)
    
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    
    return node

def search(node, target):
    """ค้นหาค่าใน BST"""
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

def minValueNode(node):
    """หาค่าต่ำสุดใน subtree"""
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, data):
    """ลบ node ออกจาก BST"""
    if not node:
        return None
    
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # เจอ node ที่จะลบแล้ว
        
        # กรณี 1: ไม่มีลูก หรือมีลูกข้างเดียว
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        
        # กรณี 2: มีลูกทั้ง 2 ข้าง
        # หา successor (ค่าถัดไปที่น้อยที่สุดใน right subtree)
        successor = minValueNode(node.right)
        node.data = successor.data
        node.right = delete(node.right, successor.data)
    
    return node

def inOrderTraversal(node):
    """แสดงค่าทั้งหมดแบบเรียงลำดับ"""
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

# ===== ทดสอบ BST =====

# สร้าง BST:
#       13
#      /  \
#     7    15
#    / \   / \
#   3  8 14  19
#            /
#           18

root = TreeNode(13)
root = insert(root, 7)
root = insert(root, 15)
root = insert(root, 3)
root = insert(root, 8)
root = insert(root, 14)
root = insert(root, 19)
root = insert(root, 18)

print("BST In-order (เรียงลำดับ): ")
inOrderTraversal(root)
print("\n")

# ทดสอบค้นหา
result = search(root, 15)
if result:
    print(f"✓ พบค่า {result.data} ใน BST")
else:
    print("✗ ไม่พบค่าใน BST")

result = search(root, 100)
if result:
    print(f"✓ พบค่า {result.data} ใน BST")
else:
    print("✗ ไม่พบค่า 100 ใน BST")

print()

# ทดสอบหาค่าต่ำสุด
print(f"ค่าต่ำสุดใน BST: {minValueNode(root).data}")
print()

# ทดสอบลบ node
print("ลบ node 15...")
root = delete(root, 15)
print("BST หลังลบ 15: ")
inOrderTraversal(root)
print()