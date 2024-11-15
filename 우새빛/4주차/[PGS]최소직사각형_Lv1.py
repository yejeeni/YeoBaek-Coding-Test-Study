def solution(sizes):
    answer = 0
    
    #가로가 더 긴 명함 / 새로가 더 긴 명함의 일관화 필요
    #명함 = A X B (단, A를 더 긴 쪽으로 고정할 것)일 때 A, B의 최대값 구하기
    
    max_a = 0; max_b = 0
    
    for s in sizes:
        if s[0] > s[1]:
            a = s[0]; b = s[1]
        else:
            a = s[1]; b = s[0]
        if max_a < a:
            max_a = a
        if max_b < b:
            max_b = b
    
    answer = max_a * max_b
    
    return answer

def solution2(sizes): #다른 사람들의 풀이, 원리는 같지만 코드 수가 적다.
    max_a = 0 ;max_b = 0
    
    for a, b in sizes:
        if a < b:
            a, b = b, a
        max_a = max(max_a, a)
        max_b = max(max_b, b)
        
    return max_a * max_b

def solution3(sizes): #다른 사람들의 풀이, 원리는 같지만 코드가 훨씬 간결하다.
                      #위의 코드들과 같이 시간복잡도는 O(n)이지만 for문을 2번 순회하므로 효율이 제일 떨어짐.
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)