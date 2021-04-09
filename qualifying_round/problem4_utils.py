from collections import deque
global q
q = 0

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

def partition(arr, chunk_size):
    return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

def get_median(arr):
    global q
    q += 1
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy[1]

def merge_basic(left, right):
    if not left:
        return right

    if not right:
        return left

    both = left.copy()

    for item in right:
        both = insert_from_rhs(both, item, 0)

    return both

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

def merge_smart2(left, right): # Not working :(
    if not left:
        return right

    if not right:
        return left

    if len(left) == 1:
        return insert_from_rhs(right, left[0], 0)

    if len(right) == 1:
        return insert_from_rhs(left, right[0], 0)

    # Make sure left is always smaller
    if len(left) > len(right):
        tmp = left
        left = right
        right = tmp

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
        l = leftq.popleft()
        r = rightq.popleft()
        last = both[-1]

        median = get_median([l, r, last])
        if median == l:
            both.insert(-1, r)
            both.insert(-1, l)
            both = insert_from_rhs(both, None, 2)
        elif median == r:
            both.insert(-1, l)
            both.insert(-1, r)
        elif median == last:
            both.insert(-1, l)
            both.append(r)

    while rightq:
        nxt = rightq.popleft()
        both = insert_from_rhs(both, nxt, 0)

    return both

if __name__ == "__main__":
    sample = [45, 28, 35, 38, 31, 26, 10, 23, 42, 49, 14, 39, 7, 27, 17, 29, 43, 30, 24, 25, 2, 41, 11, 50, 32, 46, 47, 21, 8, 13, 1, 20, 18, 36, 19, 33, 37, 3, 40, 9, 34, 6, 5, 15, 44, 12, 4, 22, 48, 16]

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
                new_partitions.append(merge_smart2(partitions[i], partitions[i+1]))
            else:
                new_partitions.append(partitions[i])
        partitions = new_partitions

    print("DONE:", *partitions[0])

    print("q: ", q)
