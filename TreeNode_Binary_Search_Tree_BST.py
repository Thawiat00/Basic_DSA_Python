class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# สร้าง tree
root = TreeNode('R')
root.left = TreeNode('A')
root.right = TreeNode('B')
root.left.left = TreeNode('C')
root.left.right = TreeNode('D')

#       R
#      / \
#     A   B
#    / \
#   C   D


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return BSTNode(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    
    return root

def search(root, target):
    if root is None or root.data == target:
        return root
    
    if target < root.data:
        return search(root.left, target)
    else:
        return search(root.right, target)

# สร้าง BST
root = None
values = [50, 30, 70, 20, 40, 60, 80]

for val in values:
    root = insert(root, val)

#         50
#        /  \
#      30    70
#     / \   / \
#   20  40 60  80

# ค้นหา
result = search(root, 40)
print("เจอ:", result.data if result else "ไม่เจอ")