from LinkedList.linked_list import LinkedList
from LinkedList.Node import Node
import typing as tp

_Set = tp.TypeVar('_Set', bound="Set")
class Set(LinkedList):
  def join(self, set: _Set) -> int:
    for set_element in set:
      for self_element in self:
        if set_element is self_element: continue
        else: self.ins_next(None, set_element.data)
    # for for
    return 0

  def conjoint(self, set: _Set) -> int:
    prev: Node = None
    for set_element in set:
      for self_element in self:
        prev = self_element
        if set_element is self_element:
          continue
        else:
          self.rem_next(prev)
      # for for
    return 0

  def injoin(self, set):
    prev: Node = None
    for set_element in set:
      for self_element in self:
        prev = self_element
        if set_element is self_element:
          self.rem_next(prev)
        else:
          continue
      # for for
    return 0
# Set()