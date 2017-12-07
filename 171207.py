# Reverse polish notation calculator
def calc(expr):
    expr = expr.split()
    stack = []
    for i in range(len(expr)):
        try:
            float(expr[i])
            stack.append(float(expr[i]))
        except:
            a, b = float(stack[-2]), float(stack[-1])
            stack.pop()
            stack.pop()
            c = 0
            if expr[i] == '+':
                c = a + b
            if expr[i] == '-':
                c = a - b
            if expr[i] == '*':
                c = a * b
            if expr[i] == '/':
                c = a / b
            stack.append(c)

    return stack.pop()


print(calc("1 2 3.5"))