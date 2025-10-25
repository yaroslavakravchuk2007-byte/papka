
# по сути это же просто алг-м Декстра?????????


def to_rpn(e):
   
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []      
    output = []     

    for c in e:
        if c.isdigit():              
            output.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':               
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()               
        elif c in priority:           
            while (stack and stack[-1] in priority and
                   priority[stack[-1]] >= priority[c]):
                output.append(stack.pop())
            stack.append(c)

    
    while stack:
        output.append(stack.pop())

   
    return ' '.join(output)



e = "(3+4*(2-1))/5"
print("Обычное выражение:", e)
print("Обратная польская нотация:", to_rpn(e))