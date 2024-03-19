from Node import Node

class BinaryTree:
  size: int
  root: Node = None
  match = None
  destroy = None

  def __init__(self, match, destroy):
    self.size = 0
    self.match = match
    self.destroy = destroy

  def isEmpty(self) -> bool:
    return self.root is None

  def ins_left(self, node, data) -> int:
    new_node = Node(data)
    node.left = new_node
    self.size += 1
    return 0

  def ins_right(self, node, data) -> int:
    new_node = Node(data)
    node.right = new_node
    self.size += 1
    return 0

  def rem_left(self, node) -> int:
    left = node.left
    if left is not None:
      self.rem_left(left)
      self.rem_right(left)
      self.destroy(left)
      node.left = None
      self.size -= 1
      return 0

    return 1

  def rem_right(self, node) -> int:
    right = node.right
    if right is not None:
      self.rem_left(right)
      self.rem_right(right)
      self.destroy(right)
      node.right = None
      self.size -= 1
      return 0

    return 1
# BinaryTree
