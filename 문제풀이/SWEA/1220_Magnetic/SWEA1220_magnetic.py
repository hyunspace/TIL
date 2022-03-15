import sys; sys.stdin = open('SWEA1220_input.txt')

'''
1. 열 중심 탐색  / 1==N, 2==S
2. 1(N)을 만나면 2(S)를 만날 때까지
 > 못 만나면 ㅂㅂ
 > 만나면 +1
  > 새로운 새로운 N을 만나면 리셋후 다시 S찾기
3. S을 만나도 N을 만날 때까지 탐색!
'''

for tc in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 최종 반환할 값 (교착 상태 개수)
    result = 0
    for j in range(N): # 열 고정
        stack = []  # 새로운 열 탐색 전 초기화
        for i in range(N): # 행 순회
            if board[i][j] == 1: # N이 나오면 담아두고
                stack.append(board[i][j])
            elif board[i][j] == 2 and len(stack) > 0 and stack[-1] == 1:
                # S가 나왔을 때 stack의 마지막 값으로 1이 담겨 있다면
                # 교착 상태 +1
                result += 1
                stack = [] # 초기화
    print(f'#{tc} {result}')



