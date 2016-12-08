# Reverse Polish Notation calculator
# based on http://en.wikipedia.org/wiki/Reverse_Polish_notation

# Steps
# - get input from user
# - parse input, put operands in stack and evaluate operators
# - maintain loop and output result

import math
import operator

ops = { '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        'sin': math.sin,
        'tan': math.tan,
        'cos': math.cos,
        'pi': math.pi }

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def calculate(equation):
    stack = []
    result = 0

    for i in equation:
        if is_number(i):
            stack.insert(0, float(i))
        else:
            if len(stack) < 2:
                print("Error: not enough values")
                break
            else:
                print('stack: {}'.format(stack))
                if len(i) == 1:
                    n1 = stack.pop(1)
                    n2 = stack.pop(0)
                    result = ops[i](n1, n2)
                    stack.insert(0, result)
                else:
                    n1 = stack.pop(0)
                    result = ops[i](math.radians(n1))
                    stack.insert(0, result)

    return result

def main():
    equation = input('Enter the equation with spaces: ').split(' ')
    answer = calculate(equation)
    print('Result: {}'.format(answer))

if __name__ == '__main__':
    main()
