class TreeNode: 
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

node0.left = node1
node0.right = node2

tree = node0
print(tree.key)
print(tree.left.key)
print(tree.right.key)

