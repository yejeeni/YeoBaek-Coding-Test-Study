# array의 i번째에서 j번째까지 자르고 정렬했을 때, k번째 수?

def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        sliced_arr = array[i-1:j]
        sliced_arr.sort()
        answer.append(sliced_arr[k-1])
    
    return answer