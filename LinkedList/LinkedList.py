class Node:
  data: None
  next: None

  def __init__(self, data): self.data = data
# Node

class LinkedList:
  size = 0
  head, tail = None, None

  def __init__(self, match, destroy):
    self.match = match
    self.destroy = destroy
  # __init__():

  def ins_next(self, node: Node, data) -> int:
    new_node = Node(data)
    if self.size == 0 and node is None: self.head = new_node
    new_node.next = node.next
    node.next = new_node
    self.size += 1
    return 0
  # __init__():

  def rem_next(self, node: Node) -> Node and None:
    old_node = node.next
    if self.size == 0: return None
    if old_node.next is None: self.tail = None
    node.next = old_node.next
    self.size -= 1
    return self.destroy(old_node)
  # rem_next():

# LinkedList
