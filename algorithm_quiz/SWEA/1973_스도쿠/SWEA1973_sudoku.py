import sys; sys.stdin = open('SWEA1973_input.txt')

# 9*9 스도쿠를 확인하는 함수
def sudoku_check(arr):
    for i in range(9): # 행고정
        check = [0] * 9 # 카운팅 정렬을 위한 빈 리스트
        for j in range(9):
            for idx in range(1, 10):
                if idx == arr[i][j]:
                    check[idx-1] += 1
        # 카운팅 정렬한 리스트 내에 1보다 큰 값이 있다?
        # => 하나가 두 번 나온 것
        if max(check) > 1:
            return False
    return True

# 3*3 스도쿠를 확인하는 함수
def tt_check(arr):
    # (0,0), (0,3), (0,6), ..., (6,6)이 시작점
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            check = [0] * 9
            # 가로세로 3
            for k in range(3):
                for l in range(3):
                    # 카운팅 정렬
                    for idx in range(1, 10):
                        if idx == arr[i + k][j + l]:
                            check[idx-1] += 1
            if max(check) > 1:
                return False
    return True

T = int(input())
for tc in range(1, 11):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    # print(puzzle)

    # 가로로 탐색
    row_check = sudoku_check(puzzle)

    # 세로로 탐색 => 전치 행렬 사용
    col_puzzle = list(map(list, zip(*puzzle)))
    col_check = sudoku_check(col_puzzle)

    # 3*3 탐색
    tbyt_check = tt_check(puzzle)

    # 최종 출력
    print(f'#{tc} {row_check * col_check * tbyt_check}')