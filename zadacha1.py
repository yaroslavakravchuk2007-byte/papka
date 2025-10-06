s = input().strip()

p = s.split("student_")[1:]  
students = []

for x in p:
    num = p[:3]
    score = int(p[3:])
    students.append((num, score))

max_score = max(score for _, score in students)
winners = [num for num, score in students if score == max_score]

print("-".join(winners))
