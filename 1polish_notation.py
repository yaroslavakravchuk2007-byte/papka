def to_postfix(e):
    p = {'+':1, '-':1, '*':2, '/':2}
    s, out = [], ''
    for c in e:
        if c.isdigit():
            out += c
        elif c == '(':
            s.append(c)
        elif c == ')':
            while s[-1] != '(':
                out += s.pop()
            s.pop()
        elif c in p:
            while s and s[-1] in p and p[s[-1]] >= p[c]:
                out += s.pop()
            s.append(c)
    while s:
        out += s.pop()
    return out

def to_prefix(e):
    e = e[::-1].replace('(', 'x').replace(')', '(').replace('x', ')')
    return to_postfix(e)[::-1]

e = "(3+4*(2-1))/5"
print("RPN:", to_postfix(e))
print("PN :", to_prefix(e))
