def solution(s):
    answer = []
    x_num = 0
    i = 0
    while len(s) > 1:
        x = s.count("0")  # 0개수 세서
        x_num += x        # 누적시키고
        s = format((len(s) - x), 'b')  #(전체길이-0개수)의 2진수를 다시 s로
        i += 1      #횟수 저장
        
    answer = [i, x_num]
    return answer

#O(n log n)