from itertools import combinations

def solution(number, k): #테스트 3~10 시간초과
    answer = ''
    
    #k개의 수를 제거하는 경우의 수 -> 조합 이용
    #combinations(number, k) / 결과:<itertools.combinations object at 0x7f...> 
    #                          (미리 생성 X, 필요할 때 생성해주는 객체 
    #                           -> 루프 사용 or 리스트로 변환 필수)
    #list(combinations(number, k)) / 결과:[('1','9'), ('1', '2')]
    combi = [list(c) for c in combinations(number, len(number)-k)]
    
    #각 경우에 만들 수 있는 큰 수
    big_num_list = []
    for c in combi:
        big_num_list.append(str(int(''.join(c))))
    
    #가장 큰 수
    answer = max(big_num_list)
    
    return answer
#combinations을 이용해 모든 경우의 수를 생성하면 조합의 개수가 매우 많아 비효율적...

def solution2(number, k):
    answer = ''
    stack = []  # 최적의 숫자를 유지하는 스택

    for num in number:
        while stack and k > 0 and stack[-1] < num: #스택에 든 숫자보다 현재수가 더 크다면 스택 제거
            stack.pop()
            k -= 1
        
        stack.append(num)  #차례대로 스택에 추가

    if k > 0:
        stack = stack[:-k] #k자리수 만큼만 남기기

    answer = ''.join(stack)
    return answer