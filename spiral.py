from pprint import pprint

def spiral_mtrx(size):
    mtrx = [[1]]
    num = 2
    for i in range(1, size):
        if i & 1:
            for row in mtrx:
                row.append(num)
                num += 1

            mtrx.append(list(range(num + i, num - 1, -1)))
            num += i + 1
        else:
            for row in reversed(mtrx):
                row.insert(0, num)
                num += 1

            mtrx.insert(0, list(range(num, num + i + 1)))
            num += i + 1
    return mtrx

n = int(input("Введите размер: "))
spiral = spiral_mtrx(n)

res = [[x * (i+1) for x in row] for i, row in enumerate(spiral)]

pprint(res, width=30)