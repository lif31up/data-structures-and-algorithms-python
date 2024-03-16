from LinkedList import LinkedList

class Stack(LinkedList):
  list: LinkedList
  max_length: int

  def __init__(self, match, destroy, max_length):
    self.list = LinkedList(match, destroy)
    self.max_length = max_length

  def isEmpty(self) -> bool: return self.list.size == 0
  def isFull(self) -> bool: return self.list.size == self.max_length

  def __check(self): return self.match is None and self.destroy is None

  def push(self, data) -> int:
    if self.isFull(): print("stack is full.")
    if self.list.insNext(None, data): return 0

  def pop(self):
    if self.isEmpty(): print("stack is empty.")
    penultimate = self.list.getPenultiamte()
    return self.list.remNext(penultimate)
# Stack