def solve_system(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    # прямой ход
    for i in range(n):
        
        div = matrix[i][i]
        for j in range(i, m):
            matrix[i][j] /= div
        
       
        for k in range(i+1, n):
            factor = matrix[k][i]
            for j in range(i, m):
                matrix[k][j] -= factor * matrix[i][j]
    
   
    res = [0] * n
    for i in range(n-1, -1, -1):
        res[i] = matrix[i][-1] - sum(matrix[i][j] * res[j] for j in range(i+1, n))
    return res