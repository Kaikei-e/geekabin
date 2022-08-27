from typing import List


class ItemInfo:
    name: str
    description: str = None
    price: float = None
    tax: float = None
    tags: List[str] = []
