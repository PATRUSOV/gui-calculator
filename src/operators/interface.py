from abc import ABC, abstractmethod
from typing import Optional


class IOperator(ABC):
    SYMBOL: Optional[str] = None
    OPERAND_COUNT: Optional[int] = None

    @classmethod
    @abstractmethod
    def compute(cls, *args: int) -> int: ...
