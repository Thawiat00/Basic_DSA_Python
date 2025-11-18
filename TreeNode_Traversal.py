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


# In-order Traversal (ซ้าย-กลาง-ขวา)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

# Pre-order Traversal (กลาง-ซ้าย-ขวา)
def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

# Post-order Traversal (ซ้าย-ขวา-กลาง)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

# ทดสอบ
print("In-order:")
inorder(root)     # C A D R B

print("\nPre-order:")
preorder(root)    # R A C D B

print("\nPost-order:")
postorder(root)   # C D A B R