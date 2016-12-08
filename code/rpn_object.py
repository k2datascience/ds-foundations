# Reverse Polish Notation Calculator
# https://en.wikipedia.org/wiki/Reverse_Polish_notation
# 34+ = 3+4 = 7

class RPNCalculator():
    """Reverse polish notation calculator"""

    def __init__(self, stack=[]):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def value(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        if len(self.stack) == 0:
            print("Calculator is empty")
            quit()
        else:
            value = self.stack.pop()
            return value

    def plus(self):
        self.stack.append(self.pop() + self.pop())

    def times(self):
        self.stack.append(self.pop() * self.pop())

    def minus(self):
        second = self.pop()
        first = self.pop()
        self.stack.append(first - second)

    def divide(self):
        second = self.pop()
        first = self.pop()
        self.stack.append(first / second)

if __name__ == "__main__":
    calc = RPNCalculator()
    calc.push(2)
    calc.push(3)
    calc.push(4)
    calc.divide()
    print(calc.value())
    calc.times()
    print(calc.value())
