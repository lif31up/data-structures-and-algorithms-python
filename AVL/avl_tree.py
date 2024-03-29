## --pending--

from avl_node import AVLNode
from BinaryTree.bst import BST

class AVLTree(BST):
  def __rotate_left(self, node):
    left = node.left
    grandchild = node.grandchild

    if left.factor is -1: ## LL Rotation
      node.left = node.right
      node.right = left
      node.factor = 0
      node.left.factor = 0
    # if

    return 0

  def __rotate_right(self, node):
    right = node.right
    grandchild = node.grandchild

    if right.factor is -1:  ## LL Rotation
      node.left = node.left
      node.left = right
      node.factor = 0
      node.right.factor = 0
    # if

    return 0