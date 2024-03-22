from LinkedList.linked_list import LinkedList
import typing as tp

class Queue:
  max_length: int
  list: LinkedList

  def __init__(self, match: tp.Callable, destroy: tp.Callable, max_length: int):
    self.list = LinkedList(match, destroy)
    self.size = max_length

  def isEmpty(self) -> bool: return self.list.size == 0
  def isFull(self) -> bool: return self.list.size == self.max_length

  def __check(self): return self.list.match is None and self.list.destroy is None

  def enqueue(self, data: object):
    if self.isFull(): print("stack is full.")
    if self.list.ins_next(None, data): return 0

  def dequeue(self):
    if self.isEmpty(): print("stack is empty.")
    return self.list.rem_next(None)
# Queue
