def solution(phone_book):
    s = set(phone_book)
    
    for number in phone_book:
        for i in range(1, len(number)):   #i번째에서 맨 첫번째는 안되니까 1부터 시작, 마지막 글자 확인 필요 x
            prefix = number[:i]  #첫번째부터 i번째까지
            if prefix in s:
                return False
    return True

#해시 쓰는 방법 시간복잡도 O(n × L)



"""
def solution(phone_book):
    phone_book.sort()   #문자열이라 사전식으로 정렬됨 => 유사한 대로 모임
    
    for i in range(len(phone_book) - 1):  #개수보다 하나 적게 반복(마지막은 필요 x)
        if phone_book[i+1].startswith(phone_book[i]): #현재 번호와 다음 번호 확인
            return False   #현재번호가 다음번호로 시작한다면 false
    return True

#시간복잡도 O(n log n * L)  L은 번호길이라 20이 최대
"""