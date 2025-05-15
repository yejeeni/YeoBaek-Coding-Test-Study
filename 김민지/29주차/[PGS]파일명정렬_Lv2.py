import re  #문자열에서 특정한 패턴을 찾거나, 추출하거나, 치환할 때 사용하는 도구

def 분해(file):
    match = re.match(r"([^\d]+)(\d{1,5})", file)  #숫자가 아닌 문자 / 1~5자리의 숫자
    head = match.group(1)   #첫번째 괄호  ([^\d]+) 에 해당
    number = match.group(2)  #두번째 괄호 (\d{1,5}) 에 해당
    return (head.lower(), int(number), file)  #헤드, 넘버, 파일명

def solution(files):
    분해리스트 = [분해(file) for file in files]  
    #print(분해리스트)
    정렬리스트 = sorted(분해리스트, key=lambda x: (x[0], x[1]))  #헤드, 넘버 순으로 정렬
    print(정렬리스트)
    return [file[2] for file in 정렬리스트]