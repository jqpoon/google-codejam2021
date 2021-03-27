t = int(input())
p = int(input())
length = 10000
players = 100

def solve():
    # setup transposed matrix
    trans = []
    for i in range(length):
        trans.append([])
    arr = []
    
    # setup normal matrix and transposed matrix
    for i in range(players):
        line = list(map(lambda x: int(x), list(input())))
        arr.append(line)

        for j in range(length):
            trans[j].append(line[j])

    # expected score for each question
    expected = []
    for i in range(length):
        tmp = sum(trans[i]) / players
        expected.append(tmp)

    # how much player deviated from average
    deviation = []
    for i in range(players):
        player_x = arr[i]
        player_x_totals = 0
        for i in range(length):
            player_x_totals += player_x[i] - expected[i]

        deviation.append(player_x_totals)

    return deviation.index(max(deviation)) + 1

for i in range(t):
    cheater = solve()
    print("Case #" + str(i+1) + ": " + str(cheater))