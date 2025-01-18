def solution(lottos, win_nums):
    answer = [0] *2 
    rank = [6,6,5,4,3,2,1]
    
    #lottos중에 win_nums랑 겹치는 리스트
    correct = [n for n in lottos if n in win_nums] 

    zero = lottos.count(0)  # 0 개수
    
    answer[0] = rank[len(correct) + zero]  # 최고순위
    answer[1] = rank[len(correct)]         # 최저순위
    
    
    return answer