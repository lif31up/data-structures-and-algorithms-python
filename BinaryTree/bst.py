from BinaryTree.bst_node import BSTNode
from BinaryTree.binary_tree import BinaryTree
import typing as tp

class BST(BinaryTree):
  match: tp.Callable

  def __init__(self, match:tp.Callable, destroy:tp.Callable):
    self.match = match
    super().__init__(destroy)

  def isEmpty(self) -> bool: return self.root is None

  def bst_search(self, key) -> list:
    class Result:
      node: BSTNode
      loc: int
      def __init__(self): self.success: bool = False

    def search(_key: int, curr_node: BSTNode, result_handler: Result):
      result = self.match(_key, curr_node.key)
      if result is 0:
        result_handler.loc = 0
        result_handler.node = curr_node
      elif result is 1:  # key1 is bigger than key2
        if curr_node.left is None:
          result_handler.loc = -1
          return 0
        search(_key, curr_node.left, result_handler)
      elif result is -1:  # key1 is smaller than key2
        if curr_node.right is None:
          result_handler.loc = 1
          return 0
        search(_key, curr_node.right, result_handler)
      return 1
    # search

    result = Result()
    if search(key, self.root, result) is 1: return 1
    return [result.node, result.loc]
  def insert(self, key, data):
    [target, loc] = self.bst_search(key)
    if loc is -1:
      target.left = BSTNode(data)
      target.left.key = key
    elif loc is 1:
      target.right = BSTNode(data)
      target.right = key
    else: return 1
    return 0

  def remove(self, key) -> object | None:
    [target, loc] = self.bst_search(key)
    if loc is not 0: return None
    return target.node
# BST
