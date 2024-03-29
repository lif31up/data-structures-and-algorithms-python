from bst_node import BSTNode
import typing as tp

class BinaryTree:
  size: int; root: BSTNode; dict = dict();
  destroy: tp.Callable;

  def __init__(self, destroy: tp.Callable):
    self.size = 0
    self.destroy = destroy

  def isEmpty(self) -> bool:
    return self.root is None

  def ins_left(self, node: BSTNode, data: object) -> int:
    new_node = BSTNode(data)
    node.left = new_node
    self.size += 1
    return 0

  def ins_right(self, node: BSTNode, data: object) -> int:
    new_node = BSTNode(data)
    node.right = new_node
    self.size += 1
    return 0

  def rem_left(self, node: BSTNode) -> int:
    left = node.left
    if left is not None:
      self.rem_left(left)
      self.rem_right(left)
      self.destroy(left)
      node.left = None
      self.size -= 1
      return 0
    # if

    return 1

  def rem_right(self, node: BSTNode) -> int:
    right = node.right
    if right is not None:
      self.rem_left(right)
      self.rem_right(right)
      self.destroy(right)
      node.right = None
      self.size -= 1
      return 0
    # if

    return 1

  def search(self, key: int) -> BSTNode:
    class Result:
      node: BSTNode

      def __init__(self):
        self.success: bool = False
    # Result

    def search(key_value: int, curr_node: BSTNode, result_node: Result) -> int:
      if key_value is curr_node.key:
        result_node.success = True
        result_node.node = curr_node
        return 0
      else:
        search(key_value, curr_node.left, result_node)
        search(key_value, curr_node.right, result_node)
      return 1

    # search
    result = Result()
    search(key, self.root, result)
    return result.node
# BinaryTree