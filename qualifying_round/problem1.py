tests = int(input())

def solve():
    n = int(input()) # list length
    line = list(map(lambda x: int(x), input().split()))
    original = line.copy()

    count = 0
    for i in range(len(line) - 1):
        j = line.index(min(line[i:]))
        line = line[:i] + line[i:j+1][::-1] + line[j+1:]
        count += (j - i + 1)

    return count

for i in range(tests):
    count = solve()
    print("Case #" + str(i+1) + ": " + str(count))

# Reversort(L):
#   for i := 1 to length(L) - 1
#     j := position with the minimum value in L between i and length(L), inclusive
#     Reverse(L[i..j])