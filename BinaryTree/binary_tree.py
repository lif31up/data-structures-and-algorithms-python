from Node import Node


class BinaryTree:
  size: int
  root: Node
  match = None
  destroy = None

  def __init__(self, match, destroy):
    self.size = 0
    self.match = match
    self.destroy = destroy

  def isEmpty(self) -> bool:
    return self.root is None

  def ins_left(self, node: Node, data: object) -> int:
    new_node = Node(data)
    node.left = new_node
    self.size += 1
    return 0

  def ins_right(self, node: Node, data: object) -> int:
    new_node = Node(data)
    node.right = new_node
    self.size += 1
    return 0

  def rem_left(self, node: Node) -> int:
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

  def rem_right(self, node: Node) -> int:
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

  def search(self, key: int) -> Node:
    class Result:
      node: Node

      def __init__(self):
        self.success: bool = False

    # Result
    def search(key_value: int, curr_node: Node, result_node: Result) -> int:
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
