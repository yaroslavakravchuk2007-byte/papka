def mnk(x, y):
    n = len(x)
    avg_x = sum(x) / n
    avg_y = sum(y) / n
    
   
    a = sum((x[i] - avg_x) * (y[i] - avg_y) for i in range(n)) / \
        sum((x[i] - avg_x) ** 2 for i in range(n))
    b = avg_y - a * avg_x
    
    return a, b 