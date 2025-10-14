from .node import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def get_height(self):
       def _height(node):
           if node is None:
            return -1 
           left_height = _height(node.left)
           right_height = _height(node.right)
           return 1 + max(left_height, right_height)
       return _height(self.root)
