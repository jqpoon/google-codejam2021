tests = int(input())

def solve():
    line = list(input().split())

    x = int(line[0])
    y = int(line[1])
    s = line[2]

    qnmark_count = s.count('?')
    c_count = s.count('C')
    j_count = s.count('J')

    # no ?s so the cost is already known
    if qnmark_count == 0:
        return x * s.count('CJ') + y * s.count('JC')

    # only Js so just fill all the ?s with Js
    if c_count == 0:
        return 0

    # only Cs
    if j_count == 0:
        return 0

    # only ?s
    if c_count == 0 and j_count == 0:
        return 0

    s = list(s)
    start_idx = -1
    end_idx = -1
    saved = ''

    for i in range(len(s)):
        if s[i] == 'C' or s[i] == 'J':
            continue
        
        assert s[i] == '?'

        # start of string
        if i == 0:
            nxt = s[1]
            if nxt == 'C':
                s[0] = 'C'
            elif nxt == 'J':
                s[0] = 'J'
            elif nxt == '?':
                start_idx = 0
                end_idx = 0
            continue

        # end of string
        if i == len(s) - 1:
            prev = s[i - 1]
            if prev == 'C':
                s[i] = 'C'
            elif prev == 'J':
                s[i] = 'J'
            elif prev == '?':
                end_idx = i
                s[start_idx : end_idx + 1] = saved * (end_idx - start_idx + 1)
                saved = ""
            continue

        prev = s[i - 1]
        curr = s[i]
        nxt = s[i + 1]

        # C?J - no difference if we choose C or J
        if prev == 'C' and curr == '?' and nxt =='J':
            s[i] = 'C'
            continue

        # J?C - no difference if we choose C or J
        if prev == 'J' and curr == '?' and nxt =='C':
            s[i] = 'C'
            continue

        # ??? - middle of a string of ?s
        if prev == '?' and curr == '?' and nxt == '?':
            end_idx += 1
            continue

        # C?? - start of a sequence of ?s
        if curr == '?' and nxt == '?':
            start_idx = i
            saved = prev
            continue

        if prev == '?' and curr == '?':
            if not saved:
                end_idx = i
                s[start_idx : end_idx + 1] = nxt * (end_idx - start_idx + 1)
                continue

            # C???C or J????J
            if nxt == saved:
                end_idx = i
                s[start_idx : end_idx + 1] = saved * (end_idx - start_idx + 1)
                saved = ""
                continue
            
            # C???J or J???C - no difference
            end_idx = i
            s[start_idx : end_idx + 1] = saved * (end_idx - start_idx + 1)
            saved = ""
            continue

    s = ''.join(s)
    return x * s.count('CJ') + y * s.count('JC')


for i in range(tests):
    count = solve()
    print("Case #" + str(i+1) + ": " + str(count))