student_heights = input().split()

for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n]) 
    
avg = 0
count = 0
for height in student_heights:
    avg += height
    count += 1

print(f"total height = {avg}\nnumber of students = {count}\naverage height = {round(avg / count)}")