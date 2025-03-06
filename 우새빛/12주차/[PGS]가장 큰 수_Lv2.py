def solution(numbers):
    answer = ''
    
    str_numbers = list(map(str, numbers)) #리스트의 정수를 문자열로 변환
    
    str_numbers.sort(key=lambda x: x*6, reverse=True) #숫자를 6번 반복해서 비교 (자리수 차이 해결을 위해) / 내림차수로 정렬
    
    #answer = ''.join(str_numbers) / 테스트 11 실패 -> numbers = [0, 0, 0] 일 때, 결과가 "000"인 경우로 예상
    answer = str(int(''.join(str_numbers))) #합치기
    
    return answer

"""
참고로 "3"과 "30"의 경우 330을 만들어야 더 큰 수임.
이때, str_numbers.sort(key=lambda x: x*10, reverse=True)에서
      key=lambda x: x*6을 통해 "333333"과 "303030303030"을 비교
      사전식 비교를 통해 33이 30보다 크므로 "333333"이 더 크다고 판단

하필 6번을 반복하여 비교하도록 한 이유는 numbers의 길이는 1 이상 100,000 이하로 최대 6자리의 숫자가 올 수 있기 때문. 
"""