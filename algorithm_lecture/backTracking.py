# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
N = 4 # 1부터 N까지 자연수 : 1, 2, 3, 4
M = 2

def backTracking(depth, at):
    if depth == M:
        ## logic
        print(*answer)
        return
    
    # 숫자 고르는 logic
    for i in range(at, len(numbers)): # i : 현재 탐색중인 index
        if not visited[i]:
            visited[i] = True # 방문표시
            answer[depth] = numbers[i] # 숫자 뽑기
            backTracking(depth + 1, i + 1)
            visited[i] = False # 잘 놀다 갑니다~


numbers = [1, 2, 3, 4]
visited = [False] * N # numbers 의 뭔가를 뽑았는지 알고 싶어서
answer = [0] * M # [1, 2]
backTracking(0, 0)