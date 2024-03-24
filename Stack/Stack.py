from LinkedList.linked_list import LinkedList
import typing as tp

class Stack:
  list: LinkedList; max_length: int;
  destroy: tp.Callable; match: tp.Callable;

  def __init__(self, match: tp.Callable, destroy: tp.Callable, max_length: int):
    self.list = LinkedList(match, destroy)
    self.max_length = max_length

  def isEmpty(self) -> bool: return self.list.size == 0
  def isFull(self) -> bool: return self.list.size == self.max_length

  def __check(self): return self.match is None and self.destroy is None

  def push(self, data) -> int:
    if self.isFull(): print("stack is full.")
    if self.list.ins_next(None, data): return 0

  def pop(self):
    if self.isEmpty(): print("stack is empty.")
    penultimate = self.list.get_penultimate()
    return self.list.rem_next(penultimate)
# Stack