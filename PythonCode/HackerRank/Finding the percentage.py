if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        a= (sum(scores))/3
        a= format(a, '.2f')
        student_marks[name] = a
    query_name = input()
    print(student_marks[query_name])
