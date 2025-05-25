def solution(numbers, target):   #깊이 우선 탐색
    answer = 0
    
    def dfs(index, current_sum):
        nonlocal answer   #바깥의 지역변수
        
        # 모든 숫자를 사용한 경우
        if index == len(numbers):
            if current_sum == target:  #답이 같으면 끝
                answer += 1
            return
        
        #숫자를 더하는 경우
        dfs(index + 1, current_sum + numbers[index])  #인덱스는 추가, 합계 계산해줌
        #숫자를 빼는 경우
        dfs(index + 1, current_sum - numbers[index])
    
    # 탐색 시작
    dfs(0, 0)
    return answer