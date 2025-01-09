def solution(numbers):
    answer = ''
    
    str_numbers = list(map(str, numbers)) #리스트의 정수를 문자열로 변환
    
    str_numbers.sort(key=lambda x: x*10, reverse=True) #숫자를 6번 반복해서 비교 (자리수 차이 해결을 위해) / 내림차수로 정렬
    
    #answer = ''.join(str_numbers) / 테스트 11 실패 -> numbers = [0, 0, 0] 일 때, 결과가 "000"인 경우로 예상
    answer = str(int(''.join(str_numbers))) #합치기
    
    return answer