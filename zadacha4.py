s = input().strip()

if len(s) < 4:
    
    if s.isupper():
        print(s.upper())
    else:
        print(s)
else:
    first_four = s[:4]
    uppercase_count = sum(1 for ch in first_four if ch.isupper())
    if uppercase_count >= 3:
        print(s.upper())
    else:
        print(s)

        