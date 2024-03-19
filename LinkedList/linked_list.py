from Node import Node

class LinkedList:
  size = 0
  head, tail = None, None

  def __init__(self, match, destroy):
    self.match = match
    self.destroy = destroy

  def ins_next(self, node: Node, data) -> int:
    new_node = Node(data)
    if self.size == 0 and node is None: self.head = new_node
    new_node.next = node.next
    node.next = new_node
    self.size += 1
    return 0

  def rem_next(self, node: Node) -> Node and None:
    if self.size == 0: return None
    if node == None:
      old_node = self.head
      self.head = self.head.next
      self.size -= 1
      if self.size == 1: self.tail = self.head
      return self.destroy(old_node)
    else:
      if node == None: return -1
      old_node = node.next
      node.next = old_node.next
      if node.next == None: self.tail = node.next
      self.size -= 1
      return self.destroy(old_node)

  def getPenultimate(self) -> Node:
    curr = self.head
    while curr.next is not None: curr = curr.next
    return curr
# LinkedList
