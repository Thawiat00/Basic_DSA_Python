class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# สร้าง tree:
#       R
#      / \
#     A   B
#    / \  / \
#   C  D E   F
#            /
#           G

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

# เชื่อมต่อ nodes
root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# ทดสอบ
print("Root's right child's left child:", root.right.left.data)  # E
print("NodeF's left child:", root.right.right.left.data)  # G