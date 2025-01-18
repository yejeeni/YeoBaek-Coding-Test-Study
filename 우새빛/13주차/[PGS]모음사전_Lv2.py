"""
A     1          1
AA    1+1        2
AAA   1+1+1      3
AAAA  1+1+1+1    4 -┐
AAAAA 1+1+1+1+1  5  |
AAAAE 1+1+1+1+2  6  |
AAAAI 1+1+1+1+3  7  | 
AAAAO 1+1+1+1+4  8  |
AAAAU 1+1+1+1+5  9 -┘
AAAE  1+1+1+7    10
  ⋮
AAAI  1+1+1+13   13
  ⋮
AAAU  1+1+1+25   28
  ⋮
AAAUU 1+1+1+25+5 33
AAE   1+1+32     34

-> 5번째 자리는  1씩 차이 
   4번째 자리는  6씩 차이 (_, A, E, I, O, U) -> 1+5*1
   3번째 자리는 31씩 차이 (_그리고 A, E, I, O, U는 각각 _, A, E, I, O, U가 있음) ->1+5*6
   그럼 2번째 자리는? 1+5*31 = 156
   그럼 1번째 자리는? 1+5*156 = 781
"""

def solution(word):
    answer = 0
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    #weight = [781, 156, 31, 6, 1]
    max_len = 5
    weight = []
    for i in range(max_len):
        if i == 0: 
            weight.append(1)
        else:
            weight.append(1 + 5 * weight[i-1]) #각 자리가 몇씩 차이나는지 가중치치
    weight.reverse()
    
    for w in range(len(word)):
        for v in range(len(vowels)):
            if word[w] == vowels[v]:
                answer += 1 + v * weight[w] #각 자리가 몇번째 단어인지 계산
                break
    
    return answer