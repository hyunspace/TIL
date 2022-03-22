'''
1. 백준이가 외치는 수는 리스트(queue)에 새롭게 추가
 - front와 rear
2. 조건에 맞춰서 front 이동해서 출력
@ 우선순위 큐
'''

N = int(input())
for _ in range(N):
    nums = []
    median = []
    n_front = n_rear = -1
    m_front = m_rear = -1

    # 백준이가 숫자를 부른다
    nums.append(int(input()))
    n_rear += 1

    # 첫번째 호출
    if n_rear == 0:
        median.append(nums[n_rear])
        m_rear += 1
        print(median[m_rear])

    # 두번째부터...
    if n_rear % 2: # 짝수번째 호출
        if median[m_rear] <= nums[n_rear]:
            print(median[m_rear])
        else:
            pass
            # median의 바로 오른쪽 값이 나와야함
    else: # 홀수번째 호출
        # if median[m_rear] <= 0
        pass