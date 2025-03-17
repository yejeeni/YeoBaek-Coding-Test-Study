def solution(sequence, k):
    answer = []
    n = len(sequence)
    i = 0
    m = 0
            
    while (m < n):        
        if sum(sequence[n-m:n:]) > k:
            n -= 1
            m = 0
        elif sum(sequence[n-m:n:]) == k:
            #print(answer[1]-answer[0])
            if len(answer) > 0 and (answer[1]-answer[0]) > m+1:
                answer = [n-m, n-1]
            if sum(sequence[n-m-1:n-1:]) == k:
                print("there's more")
                answer = [n-m-1, n-2]
                if sum(sequence[n-m-2:n-2:]) == k:
                    answer = [n-m-2, n-3]
                    print("2번")
            

        m += 1
    return answer
    
"""

def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]
    min_length = float('inf')
    answer = [-1, -1]

    while right < len(sequence):
        if current_sum == k:
            if (right - left) < min_length:
                min_length = (right - left)
                answer = [left, right]
            elif (right - left) == min_length and left < answer[0]:
                answer = [left, right]

        if current_sum < k:
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
        else:
            current_sum -= sequence[left]
            left += 1
            
    return answer
"""