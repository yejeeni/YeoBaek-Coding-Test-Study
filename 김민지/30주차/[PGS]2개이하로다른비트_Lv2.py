def solution(numbers):
    answer = []
    for n in numbers:
        #if n % 2 == 0:            #짝수인 경우 1만 증가되면 1자리수 차이가 남
        #    answer.append(n + 1)
        #else:                     #홀수인 경우 2자리 바꿔야함
            # 비트연산: f(x) = x + (x ^ (x + 1)) >> 2 + 1  #^부분을 통해 비트가 다른 곳만 1
        b = n + ((n ^ (n + 1)) >> 2) + 1
        answer.append(b)
    return answer
