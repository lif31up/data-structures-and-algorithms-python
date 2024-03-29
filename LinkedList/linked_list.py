from list_node import ListNode
import typing as tp


class LinkedList:
  size = 0
  head, tail = None, None
  match: tp.Callable
  destroy: tp.Callable
  iterator: ListNode

  def __init__(self, match: tp.Callable, destroy: tp.Callable):
    self.match = match
    self.destroy = destroy

  def __iter__(self):
    self.iterator = self.head
    return self.head

  def __next__(self) -> object:
    if self.iterator is None:
      raise StopIteration
    else:
      data: object = self.iterator.data
      self.iterator = self.iterator.next
      return data

  def ins_next(self, node: ListNode | None, data: object) -> int:
    new_node = ListNode(data)
    if self.size == 0 and node is None: self.head = new_node
    new_node.next = node.next
    node.next = new_node
    self.size += 1
    return 0

  def rem_next(self, node: ListNode | None) -> ListNode and None:
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

  def get_penultimate(self) -> ListNode:
    curr = self.head
    while curr.next is not None: curr = curr.next
    return curr
# LinkedList
