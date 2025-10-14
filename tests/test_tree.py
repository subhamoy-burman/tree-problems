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