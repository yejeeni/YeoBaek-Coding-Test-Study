def solution(phone_book):
    answer = True
    
    # 정렬 후 다음 요소에 자신이 접두사로 들어가는지 확인
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            answer = False; break
    
    return answer

def solution2(phone_book): # 다른 사람들의 풀이: 해시를 이용한 풀이...
    answer = True
    hash = {}
    
    # 각 번호들 해시로 저장
    for phone_number in phone_book:
        hash[phone_number] = 1
    
    # 전화번호부의 숫자를 하나씩 비교
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            # 만약 임시까지 저장해둔 번호와 일치하는 번호가 해시에 있는지 확인(접두사가 있는지 확인)
            # 이때 자신의 전체 번호는 당연히 해시에 저장되어 있으니 제외한다.
            if temp in hash and temp != phone_number:
                answer = False
                
    return answer
