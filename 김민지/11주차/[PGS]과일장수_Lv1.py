def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(len(score)//m):
        tmp = score[i*m:i*m+m]
        answer += (min(tmp) * m)
    return answer

#시간복잡도 O(N logN)