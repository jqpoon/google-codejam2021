tests = int(input())

def solve():
    n = int(input()) # list length
    line = list(map(lambda x: int(x), input().split()))

    count = 0
    for i in range(1, len(line)):
        tmp = 0
        while line[i] <= line[i-1]:
            count += 1
            tmp += 1
            line[i] = line[i] * 10

            curr = line[i]
            prev = line[i-1]

            # same number of digits and same first digit
            if (int(str(curr)[0]) == int(str(prev)[0])) and len(str(prev)) == len(str(curr)):
                if tmp != 1 or line[i-1] % 10 != 9:
                    line[i] = line[i-1] + 1
                    break

    assert(sorted(line) == line)

    return count

for i in range(tests):
    count = solve()
    print("Case #" + str(i+1) + ": " + str(count))