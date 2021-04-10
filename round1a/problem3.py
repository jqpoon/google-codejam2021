tests = int(input())

def solve():
    line = list(map(lambda x: int(x), input().split()))
    n = line[0] # number of students
    q = line[1] # number of questions

    all_scores = []
    for i in range(n):
        line2 = list(input().split())
        answers = list(line2[0])
        score = int(line2[1])

        if score == q:
            return (answers, score, 1)

        all_scores.append((score, answers))

    print(answers)

    z = 0
    w = 0
    return ("FFT", z, w)

for i in range(tests):
    ans, z, w = solve()
    print("Case #" + str(i+1) + ": " + "".join(ans) + " " + str(z) + "/" + str(w))