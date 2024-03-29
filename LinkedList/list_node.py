import typing as tp

_ListNode = tp.TypeVar('_ListNode', bound='ListNode')
class ListNode:
  data: object; next: _ListNode;
  def __init__(self, data: object): self.data = data