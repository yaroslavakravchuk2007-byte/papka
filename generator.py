import random

def generate_data(N, a, b, sigma=1):
    x = list(range(N))
    y = [a*xi + b + random.gauss(0, sigma) for xi in x]
    return x, y
