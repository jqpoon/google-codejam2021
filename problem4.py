import sys
line = list(map(lambda x: int(x), input().split()))
t = line[0] # number of test cases
n = line[1] # length of list
q = line[2] # total number of attempts

def partition(arr, chunk_size):
    return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

def insert_from_rhs(sort, nxt):
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

def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    both = left.copy()

    for item in right:
        insert_from_rhs(both, item)

    return both

def solve():
    sample = list(range(1, n+1))

    # Attempt some kind of merge sort
    partitions = partition(sample, 3)

    for idx, part in enumerate(partitions):
        if len(part) == 3:
            print(*part)
            median = int(input())

            last = part[-1]
            last2 = part[-2]
            last3 = part[-3]

            if median == last2:
                pass

            if median == last:
                part[-1] = last2
                part[-2] = last

            if median == last3:
                part[-3] = last
                part[-2] = last3
                part[-1] = last2
    
    # "Merge" sort
    while len(partitions) != 1:
        new_partitions = []
        for i in range(0, len(partitions), 2):
            if i+1 != len(partitions):
                new_partitions.append(merge(partitions[i], partitions[i+1]))
            else:
                new_partitions.append(partitions[i])
        partitions = new_partitions
    
    print(*partitions[0])
    assert(input() == '1')

# "Insertion" sort
def old_solve():
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
        insert_from_rhs(sort, nxt)

    print(*sort)
    assert(input() == '1')

for i in range(t):
    solve()