import sys
from collections import deque

line = list(map(lambda x: int(x), input().split()))
t = line[0] # number of test cases
n = line[1] # length of list
q = line[2] # total number of attempts

def partition(arr, chunk_size):
    return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

def get_median(arr):
    print(*arr)
    return int(input())

def insert_from_rhs(sort, nxt, pos):
    if pos == 0:
        sort.append(nxt)
    while True:
        if pos + 3 == len(sort) + 1:
            break

        last = sort[-1 - pos]
        last2 = sort[-2 - pos]
        last3 = sort[-3 - pos]

        median = get_median([last3, last2, last])

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

    return sort  

# This is not optimal, since we aren't really merging
# by taking the head of one list and the other one at a time
# There's probably a nice way of doing this, and merge_smart2 in problem4_utils
# tries this, but to no avail.
def merge_smart(left, right):
    if not left:
        return right

    if not right:
        return left

    if len(left) == 1:
        return insert_from_rhs(right, left[0], 0)

    if len(right) == 1:
        return insert_from_rhs(left, right[0], 0)

    # Start merging by getting 2 elems from lhs and one from rhs
    leftq = deque(left)
    rightq = deque(right)
    both = []

    fst = leftq.popleft()
    snd = leftq.popleft()
    trd = rightq.popleft()

    median = get_median([fst, snd, trd])
    if median == fst:
        both = [trd, fst, snd]
    elif median == trd:
        both = [fst, trd, snd]
    else:
        both = [fst, snd, trd]

    # Drain all elements from leftq first
    while leftq:
        if trd != both[-1]: # Shortcut if first element in RHS is not on the right
            both = both + list(leftq)
            break

        nxt = leftq.popleft()
        both = insert_from_rhs(both, nxt, 0)

    # Insert rest of elements in RHS normally
    while rightq:
        nxt = rightq.popleft()
        both = insert_from_rhs(both, nxt, 0)

    return both

def solve_merge():
    sample = list(range(1, n+1))

    # Attempt some kind of merge sort
    partitions = partition(sample, 3)

    for idx, part in enumerate(partitions):
        if len(part) == 3:
            median = get_median(part)

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
    
    while len(partitions) != 1:
        new_partitions = []
        for i in range(0, len(partitions), 2):
            if i+1 != len(partitions):
                new_partitions.append(merge_smart(partitions[i], partitions[i+1]))
            else:
                new_partitions.append(partitions[i])
        partitions = new_partitions
    
    print(*partitions[0])
    assert(input() == '1')

# "Insertion" sort
def solve_insertion():
    sort = []
    median = get_median([1, 2, 3])

    if median == 2:
        sort = [1, 2, 3]
    elif median == 1:
        sort = [2, 1, 3]
    elif median == 3:
        sort = [1, 3, 2]

    while len(sort) != n:
        nxt = len(sort) + 1
        insert_from_rhs(sort, nxt, 0)

    print(*sort)
    assert(input() == '1')

for i in range(t):
    solve_insertion()