N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
result = 0
visited = [[0]*M for _ in range(N)]
def find_score(cnt, score, row, col):
    global result
    if cnt == 4:
        result = max(score, result)
        return
    for d in range(4):
        nr = row + dr[d]
        nc = col + dc[d]
        if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            find_score(cnt + 1, score+board[nr][nc], nr, nc)
            visited[nr][nc] = 0

for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        score = board[r][c]
        find_score(1,score,r,c)
        visited[r][c] = 0
        for i in range(4):
            score = board[r][c]
            cnt = 0
            for j in range(4):
                nr = r + dr[j]
                nc = c + dc[j]
                if j != i and 0<=nr<N and 0 <= nc<M:
                    score += board[nr][nc]
                    cnt += 1
            if cnt == 3:
                result = max(score, result)

print(result)