import itertools
tests = int(input())

def calculate_value(n, line):
    tmp = line.copy()

    count = 0
    for i in range(len(tmp) - 1):
        j = tmp.index(min(tmp[i:]))
        tmp = tmp[:i] + tmp[i:j+1][::-1] + tmp[j+1:]
        count += (j - i + 1)

    return count

# Return list of answers if it exists, else return empty list for impossible case
def solve():
    line = list(map(lambda x: int(x), input().split()))
    n = line[0]
    c = line[1]

    # Lower than min. value
    if c < n - 1:
        return []

    # Larger than max. value
    if c > n*(n+1)/2 - 1:
        return []

    # min value
    if c == n - 1:
        return list(range(1, n + 1))
    
    # max value
    if c == n*(n+1)/2 - 1:
        ret = []
        for i in reversed(range(1, n + 1)):
            if i % 2 == 0: # even, insert at front
                ret.insert(0, i)
            else: # odd, insert at back
                ret.append(i)
        return ret

    # special case
    if c == 2*n - 2:
        return list(reversed(range(1, n+1)))

    for perm in itertools.permutations(list(range(1, n+1))):
        cost = calculate_value(n, list(perm))
        if cost == c:
            return list(perm)

    return []

for i in range(tests):
    ans = solve()
    if ans: # answer exists
        print("Case #" + str(i+1) + ":", *ans)
    else:
        print("CASE #" + str(i+1) + ": IMPOSSIBLE")