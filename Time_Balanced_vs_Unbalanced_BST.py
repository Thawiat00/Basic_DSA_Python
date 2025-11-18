import time

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    if node is None:
        return TreeNode(data)
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    return node

def search(node, target):
    if node is None:
        return None
    if node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

def tree_height(node):
    """คำนวณความสูงของ tree"""
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

# สร้าง Balanced BST
print("=== Balanced BST ===")
balanced = None
values = [50, 25, 75, 12, 37, 62, 87]
for v in values:
    balanced = insert(balanced, v)
print(f"ความสูง: {tree_height(balanced)}")

# สร้าง Unbalanced BST (แทบเป็นเส้นตรง)
print("\n=== Unbalanced BST ===")
unbalanced = None
values = [10, 20, 30, 40, 50, 60, 70]
for v in values:
    unbalanced = insert(unbalanced, v)
print(f"ความสูง: {tree_height(unbalanced)}")

# เปรียบเทียบเวลาค้นหา
print("\n=== ทดสอบความเร็วในการค้นหา ===")

start = time.time()
for _ in range(10000):
    search(balanced, 87)
balanced_time = time.time() - start

start = time.time()
for _ in range(10000):
    search(unbalanced, 70)
unbalanced_time = time.time() - start

print(f"Balanced BST: {balanced_time:.6f} วินาที")
print(f"Unbalanced BST: {unbalanced_time:.6f} วินาที")
print(f"Unbalanced ช้ากว่า: {unbalanced_time/balanced_time:.2f} เท่า")