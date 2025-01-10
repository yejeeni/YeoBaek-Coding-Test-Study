def solution(a, b, n):
    answer = 0
    while n >= a:
        get = (n // a) * b  # 얻은 수
        left = n % a        # 남은 수 = 나머지계산

        n = get + left      # 현재 가진 수 = 얻은 수 + 남은 수
        answer += get       # 얻은 만큼 더해줌
    return answer

# 시간복잡도 O(logN)