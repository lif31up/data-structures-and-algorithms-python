from LinkedList import linked_list

class Queue:
  max_length: int
  list: LinkedList

  def __init__(self, match, destroy, max_length):
    self.list = LinkedList(match, destroy)
    self.size = max_length

  def isEmpty(self) -> bool: return self.list.size == 0
  def isFull(self) -> bool: return self.list.size == self.max_length

  def __check(self): return self.list.match is None and self.list.destroy is None

  def enqueue(self, data):
    if self.isFull(): print("stack is full.")
    if self.list.insNext(None, data): return 0

  def dequeue(self):
    if self.isEmpty(): print("stack is empty.")
    return self.list.remNext(None)
# Queue
