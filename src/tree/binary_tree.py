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
    
    def get_height(self):
       def _height(node):
           if node is None:
            return -1 
           left_height = _height(node.left)
           right_height = _height(node.right)
           return 1 + max(left_height, right_height)
       return _height(self.root)

    def diameter(self):
       max_diam = 0

       def _heightAndDiameter(node):
           nonlocal max_diam
           if node is None:
            return -1 
           left_height = _heightAndDiameter(node.left)
           right_height = _heightAndDiameter(node.right)
           max_diam = max(max_diam, left_height + right_height + 2)
           return 1 + max(left_height, right_height)
       return max_diam

    def maxPathSum(self):
        maxSumOfPath = float('-inf')

        def recursionMaxPathSum(node):
            nonlocal maxSumOfPath

            if node is None:
                return 0
            
            leftMaxPathSum = recursionMaxPathSum(node.left)
            rightMaxPathSum = recursionMaxPathSum(node.right)

            sumOfPath = node.value + max(leftMaxPathSum,0) + max(rightMaxPathSum,0)
            maxSumOfPath = max(sumOfPath, maxSumOfPath)

            return node.value + max(0, leftMaxPathSum, rightMaxPathSum)
            
        recursionMaxPathSum(self.root)
        return maxSumOfPath
       
   




       
