import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from tree.node import TreeNode
from tree.binary_tree import BinaryTree
def test_tree_node_creation():
	node = TreeNode(10)
	assert node.value == 10
	assert node.left is None
	assert node.right is None

def test_binary_tree_creation():
	tree = BinaryTree()
	assert tree.root is None

def test_binary_tree_height_null():
	tree = BinaryTree()
	assert tree.get_height() == -1

def test_binary_tree_height():
	tree = BinaryTree()
	tree.root = TreeNode(1)
	tree.root.left = TreeNode(2)
	tree.root.right = TreeNode(3)
	tree.root.left.left = TreeNode(4)
	tree.root.left.right = TreeNode(5)
	# Tree structure:
	#        1
	#      /   \
	#     2     3
	#    / \
	#   4   5
	# Height (edges): 2
	assert tree.get_height() == 2

def test_binary_tree_is_balance_true():
	tree = BinaryTree()
	tree.root = TreeNode(1)
	tree.root.left = TreeNode(2)
	tree.root.right = TreeNode(3)
	tree.root.left.left = TreeNode(4)
	tree.root.left.right = TreeNode(5)

	assert tree.is_balanced() is true

def test_max_path_sum_positive():
	tree = BinaryTree()
	tree.root = TreeNode(1)
	tree.root.left = TreeNode(2)
	tree.root.right = TreeNode(3)
	tree.root.left.left = TreeNode(4)
	tree.root.left.right = TreeNode(5)
	# The max path is 4 -> 2 -> 1 -> 3, sum = 10
	assert tree.maxPathSum() == 11

def test_max_path_sum_negative():
	tree = BinaryTree()
	tree.root = TreeNode(-10)
	tree.root.left = TreeNode(-20)
	tree.root.right = TreeNode(-30)
	# The max path is -10 (single node)
	assert tree.maxPathSum() == -10

def test_max_path_sum_mixed():
	tree = BinaryTree()
	tree.root = TreeNode(-10)
	tree.root.left = TreeNode(9)
	tree.root.right = TreeNode(20)
	tree.root.right.left = TreeNode(15)
	tree.root.right.right = TreeNode(7)
	# The max path is 15 -> 20 -> 7, sum = 42
	assert tree.maxPathSum() == 42