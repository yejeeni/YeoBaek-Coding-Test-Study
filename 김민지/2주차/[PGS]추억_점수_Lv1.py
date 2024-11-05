def solution(name, yearning, photo):
    answer = []
    dic = {}  #딕셔너리 이용
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    print(dic)
        
    for i in range(len(photo)):  #사진 개수많큼 반복
        sum = 0
        for k,v in dic.items():  #key값, 즉 사람이름으로  
            if k in photo[i]:    #사진에 있는지 확인하고
                sum += v         #추억점수를 더함
        answer.append(sum)
    return answer