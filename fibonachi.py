def prime_factors(n, divisor=2, factors[]):
    if n == 1:  
        return factors
    elif n % divisor == 0 :  
        return prime_factors(n//divisor, divisor, factors+[divisor])
    else:
        return (n, divisor+1 , factors)
print(prime_factors(4))