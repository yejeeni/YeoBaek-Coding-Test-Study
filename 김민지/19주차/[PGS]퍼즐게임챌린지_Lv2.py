def find_time(diffs, times, level):
    time = 0
    for j in range(len(diffs)):
        if diffs[j] > level:
            time += (times[j]+times[j-1]) * (diffs[j]-level)
        time += times[j]
    return time

def solution(diffs, times, limit):  #이분탐색
    answer = 0
    left, right = 1, max(diffs)

    while left <= right:  
        mid = (left + right) // 2   #중간값 설정
        time = find_time(diffs, times, mid)
        print(left, right, "=>", mid, time)
         
        if time <= limit:
            answer = mid   #가능한 값 일단 저장
            print("save", mid)
            right = mid - 1
        else:
            left = mid + 1
        
    return answer