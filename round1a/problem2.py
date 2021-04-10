tests = int(input())

def solve():
    m = int(input()) # list length

    primes = []
    for i in range(m):
        line = list(map(lambda x: int(x), input().split()))
        p = line[0] # prime number
        m = line[1] # no. of cards with this prime number

        primes.append((p, m))

    print(primes)
    count = 0
    return count

for i in range(tests):
    count = solve()
    print("Case #" + str(i+1) + ": " + str(count))