tests = int(input())

def solve():
    n = int(input()) # list length
    line = list(map(lambda x: int(x), input().split()))

    count = 0
    for i in range(1, len(line)):
        while line[i] <= line[i-1]:
            count += 1
            line[i] = line[i] * 10

            if (line[i] - line[i] % 10) == (line[i-1] - line[i-1] % 10) and (line[i-1] % 10 != 9):
                line[i] = line[i-1] + 1

    print(line)
    return count

for i in range(tests):
    count = solve()
    print("Case #" + str(i+1) + ": " + str(count))