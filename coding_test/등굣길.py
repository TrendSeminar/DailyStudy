def solution(m, n, puddles):
    maps = [[0] * (m+1) for i in range(n+1)]
    maps[1][1] = 1

    for i in range(n+1):
        for j in range(m+1):
            if i == 1 and j == 1:
                continue

            if [j, i] in puddles:
                maps[i][j] = 0

            else:
                maps[i][j] += (maps[i-1][j]+maps[i][j-1])

    return maps[-1][-1] % 1000000007
