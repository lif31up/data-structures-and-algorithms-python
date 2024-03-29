import typing as tp

_AVLNode = tp.TypeVar('_AVLNode', bound="AVLNode")
class AVLNode:
  data: object
  left: _AVLNode = None; right: _AVLNode = None;
  hidden: int; factor: int

  def __init__(self, data: object, hint: int, factor: int):
    self.data = data
    self.hint = hint
    self.factor = factor
# AVLNode