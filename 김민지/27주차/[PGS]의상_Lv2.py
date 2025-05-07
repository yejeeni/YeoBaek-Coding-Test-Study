from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    
    for a, b in clothes:
        dic[b] += 1
    
    print(dic)
    for count in dic.values():
        answer *= (count + 1)  # 입는 경우 + 안 입는 경우
    answer -= 1
    
    return answer

#안입는 경우 빼고 모든 경우의 수 구하는거 ->
#상의 2개, 하의 3개면 상의 0, 1, 2 / 하의 0, 1, 2, 3의 조합에서 0,0만 빼면 됨 => 3*4-1

#머리 : 노랑모자, 눈: 선글라스, 머리 : 초록  //2, 1 => 3, 2
# 노랑 / 파랑 / 초록/ 노랑+파랑 / 노랑+초록