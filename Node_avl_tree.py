class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # AVL ต้องเก็บ height

def getHeight(node):
    """ดึงความสูงของ node"""
    if not node:
        return 0
    return node.height

def getBalance(node):
    """คำนวณ Balance Factor"""
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    """
    หมุนขวา (Right Rotation)
         y                x
        / \              / \
       x   T3    =>    T1   y
      / \                  / \
     T1  T2              T2  T3
    """
    print(f'🔄 Rotate right on node {y.data}')
    x = y.left
    T2 = x.right
    
    # หมุน
    x.right = y
    y.left = T2
    
    # อัพเดท height
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    
    return x

def leftRotate(x):
    """
    หมุนซ้าย (Left Rotation)
       x                  y
      / \                / \
    T1   y      =>      x   T3
        / \            / \
       T2  T3        T1  T2
    """
    print(f'🔄 Rotate left on node {x.data}')
    y = x.right
    T2 = y.left
    
    # หมุน
    y.left = x
    x.right = T2
    
    # อัพเดท height
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    
    return y

def insert(node, data):
    """เพิ่ม node และปรับสมดุลอัตโนมัติ"""
    
    # 1. ทำ BST insert ปกติ
    if not node:
        return TreeNode(data)
    
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    else:
        return node  # ไม่ใส่ค่าซ้ำ
    
    # 2. อัพเดท height
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    
    # 3. คำนวณ Balance Factor
    balance = getBalance(node)
    
    # 4. ถ้าไม่สมดุล ให้ rotate
    
    # Left-Left Case
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    
    # Left-Right Case
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    
    # Right-Right Case
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)
    
    # Right-Left Case
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node

def inOrderTraversal(node):
    """แสดงค่าทั้งหมดแบบเรียงลำดับ"""
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

def printTree(node, level=0, prefix="Root: "):
    """แสดง tree แบบมองเห็นโครงสร้าง"""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.data) + f" (h={node.height}, BF={getBalance(node)})")
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                printTree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# ===== ทดสอบ AVL Tree =====

print("=== สร้าง AVL Tree ===")
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']

for letter in letters:
    print(f"\n➕ Insert {letter}")
    root = insert(root, letter)

print("\n" + "="*50)
print("🌳 โครงสร้าง AVL Tree ขั้นสุดท้าย:")
print("="*50)
printTree(root)

print("\n" + "="*50)
print("📋 In-order Traversal (ต้องเรียงลำดับ A-H):")
inOrderTraversal(root)
print("\n" + "="*50)