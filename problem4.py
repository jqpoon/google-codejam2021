import sys
line = list(map(lambda x: int(x), input().split()))
t = line[0] # number of test cases
n = line[1] # length of list
q = line[2] # total number of attempts

def solve():
    sort = []
    print(1, 2, 3)
    median = int(input())

    if median == 2:
        sort = [1, 2, 3]
    elif median == 1:
        sort = [2, 1, 3]
    elif median == 3:
        sort = [1, 3, 2]

    while len(sort) != n:
        nxt = len(sort) + 1
        sort.append(nxt)

        pos = 0
        while True:
            if pos + 3 == len(sort) + 1:
                break

            last = sort[-1 - pos]
            last2 = sort[-2 - pos]
            last3 = sort[-3 - pos]

            print(last3, last2, last)
            median = int(input())

            if median == last2:
                break

            if median == last:
                sort[-1 - pos] = last2
                sort[-2 - pos] = last
                break

            if median == last3:
                if pos == 0:
                    sort[-3 - pos] = last
                    sort[-2 - pos] = last3
                    sort[-1 - pos] = last2
                    pos += 1
                else:
                    sort[-3 - pos] = last2
                    sort[-2 - pos] = last3
                    pos += 1

    print(*sort)
    assert(input() == '1')

for i in range(t):
    solve()