s = input()
result = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        result.add(s[i:j+1])

print(len(result))

"""
set이나 dict의 key에는 list를 넣을 수 없음
list는 내부 값이 바뀔 수 있어서 hash값이 변할 수 있는데, set이나 dict는 내부적으로 hash값을 기준으로 저장하기 때문
대신 tuple은 변경 불가하단 특징이 있어서 가능
"""