from typing import Dict, Type

from src.operators.interface import IOperator
from src.operators.exceptions import OperandsCountError


class OperatorInvoker:
    _ops: Dict[str, Type[IOperator]] = dict()

    @classmethod
    def add_operator(cls, operator: Type[IOperator]) -> None:
        if operator.SYMBOL is None:
            raise TypeError("Operator must define a SYMBOL.")

        if operator.OPERAND_COUNT is None:
            raise TypeError("Operands count must be defined.")

        if operator.SYMBOL in cls._ops:
            raise TypeError(f"Operator '{operator.SYMBOL}' is already registered")

        cls._ops[operator.SYMBOL] = operator  # type: ignore

    @classmethod
    def compute(cls, operator_sym: str, *args: int) -> int:
        operator = cls._ops.get(operator_sym)

        if operator is None:
            raise KeyError(f"Unknown operator: {operator_sym}")

        if len(args) != operator.OPERAND_COUNT:
            raise OperandsCountError(
                f"Operator {operator.SYMBOL} needs 2 operands, got {len(args)}."
            )

        return operator.compute(*args)
