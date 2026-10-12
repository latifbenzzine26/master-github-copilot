class Calculator:
    """Simple integer calculator."""
    def add(self, a: int, b: int) -> int:
        return a + b

    def sub(self, a: int, b: int) -> int:
        return a - b

    def mul(self, a: int, b: int) -> int:
        return a * b

    def div(self, a: int, b: int) -> float:
        return a / b  # TODO: handle divide-by-zero in tests


_calculator = Calculator()


def add(a: int, b: int) -> int:
    return _calculator.add(a, b)


def subtract(a: int, b: int) -> int:
    return _calculator.sub(a, b)


def multiply(a: int, b: int) -> int:
    return _calculator.mul(a, b)


def divide(a: int, b: int) -> float:
    return _calculator.div(a, b)
