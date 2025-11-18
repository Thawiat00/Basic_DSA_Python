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