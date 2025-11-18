class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")

# สร้าง tree ง่ายๆ:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)



print("Pre-order: ", end="")
preOrderTraversal(root)
print("\n")



print("In-order: ", end="")
inOrderTraversal(root)
print("\n")



print("Post-order: ", end="")
postOrderTraversal(root)
print()

#```

#**ผลลัพธ์ที่คาดหวัง:**
#```
#Pre-order: 1, 2, 4, 5, 3, 
#In-order: 4, 2, 5, 1, 3, 
#Post-order: 4, 5, 2, 3, 1,