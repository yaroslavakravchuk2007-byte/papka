def calc_rpn(expr):
    stack = []
    for c in expr:
        if c.isdigit():             
            stack.append(int(c))
        elif c in '+-*/':            
            if len(stack) < 2:
                return "Ошибка: неверное выражение"
            b = stack.pop()
            a = stack.pop()
            if c == '+': stack.append(a + b)
            elif c == '-': stack.append(a - b)
            elif c == '*': stack.append(a * b)
            elif c == '/':
                if b == 0:
                    return "Ошибка: деление на ноль"
                stack.append(a / b)
        else:
            return "Ошибка: недопустимый символ"

    if len(stack) == 1:
        return stack[0]
    else:
        return "Ошибка: неверное выражение"


#гениальный примерчик
print(calc_rpn("3421-*+5/"))  # (3 + 4 * (2 - 1)) / 5