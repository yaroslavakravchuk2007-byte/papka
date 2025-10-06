s = input()

length = len(s)

if length <= 2:
    print(ord(s[0]))
elif 2 < length < 10:
    middle_index = (length - 1) // 2  
    result = ord(s[0]) + ord(s[middle_index]) + ord(s[-1])
    print(result)
else:  
    print(ord(s[-1]))