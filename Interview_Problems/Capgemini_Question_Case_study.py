#Capgemini Questions
n = int(input("Enter no of semester: "))

subjects = []

for i in range(n):
    s = int(input(f"Enter no of subjects in {i+1} semester: "))
    subjects.append(s)

marks = []

for i in range(n):
    sem_marks = []
    
    print(f"Marks obtained in semester {i+1}:")
    for j in range(subjects[i]):
        m = int(input())
        if m < 0 or m > 100:
            print("You have entered invalid mark.")
            exit()
        sem_marks.append(m)
    marks.append(sem_marks)

for i in range(n):
    print(f"Maximum mark in {i+1} semester:{max(marks[i])}")
