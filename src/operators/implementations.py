from src.operators.interface import IOperator
from src.operators.invocation import OperatorInvoker


@OperatorInvoker.add_operator
class PlusOperator(IOperator):
    SYMBOL = "+"
    OPERAND_COUNT = 2

    @classmethod
    def compute(cls, *args: int) -> int:
        return args[0] + args[1]
