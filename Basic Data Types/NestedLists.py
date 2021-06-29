if __name__ == '__main__':
    students = [[input(), float(input())] for _ in range(int(input()))]
    stu = []
    low = 1000
    length = len(students)
    for i in range(len(students)):
        if students[i][1] < low:
            low = students[i][1]
    i = 0
    while i < length:
        if students[i][1] == low:
            students.remove(students[i])
            length -= 1
            i -= 1
        i += 1
    low = 1000
    for i in range(len(students)):
        if students[i][1] < low:
            low = students[i][1]
    students.sort()
    for i in range(len(students)):
        if students[i][1] == low:
            stu = students[i]
            print(stu[0])
