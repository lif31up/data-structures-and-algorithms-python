from typing import TypeVar

_Node = TypeVar('_Node', bound='Node')

class Node:
  data: object; next: _Node
  def __init__(self, data: object): self.data = data