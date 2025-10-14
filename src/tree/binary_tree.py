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
    
    def is_balanced(self):
       def check(node):
          if node is None:
           return 0
          leftBalance = check(node.left)
          if leftBalance == -1:
            return -1
          rightBalance = check(node.right)
          if rightBalance == -1:
            return -1
          if abs(leftBalance - rightBalance) > 1:
             return -1
          return 1 + max(rightBalance,leftBalance)
       return check(self.root)!= -1
       
