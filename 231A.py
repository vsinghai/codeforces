def problem_solver():
    counter = 0
    lines = int(input())
    for i in range(lines):
        one, two, three = map(int, input().split())
        counter += 1 if (one + two + three >=2) else 0
    print(counter)
    

problem_solver()