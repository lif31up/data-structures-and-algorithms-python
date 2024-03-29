import typing as tp

_BSTNode = tp.TypeVar('_BSTNode', bound="BSTNode")
class BSTNode:
  key: int; data: object
  left: _BSTNode; right: _BSTNode;

  def __init__(self, data): self.data = data
# Node