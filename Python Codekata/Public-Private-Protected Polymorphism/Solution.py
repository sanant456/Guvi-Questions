n = int(input())
max_avg = -1.0
top_student = ""
for _ in range(n):
  student = input().split()

 #....YOUR CODES STARTS HERE....
  name = student[0]
    marks = list(map(int, student[1:]))
    avg = sum(marks) / len(marks)
    
    if avg > max_avg:
        max_avg = avg
        top_student = name


#....YOUR CODES ENDS HERE....

print(top_student)
