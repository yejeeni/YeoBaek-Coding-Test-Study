import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# n개의 줄에 걸쳐 번호 순서대로 이름 입력
# m개의 줄에 입력이 들어오는데, 이름이 들어오면 번호를, 번호가 들어오면 이름을 출력해야 함

dic_by_id = {} # key가 id인 딕셔너리
dic_by_name = {} # key가 name인 딕셔너리

for id in range(1, n+1):
  name = input().strip() # .strip() : 양쪽 문자열에 공백이나 인자가된 문자열의 모든 조합을 제거
  dic_by_id[id] = name
  dic_by_name[name] = id

for i in range(m):
  pokemon = input().strip()
 
  if pokemon.isdigit(): # .isdigit() : 값이 숫자로만 있는지 검사하는 함수
    print(dic_by_id[int(pokemon)])
  else:
    print(dic_by_name[pokemon])

"""
# 처음엔 한 딕셔너리에 담아서 key, value를 뒤집은 새로운 딕셔너리를 만들으려 했는데 그럴 필요 X
# 그냥 만들 때부터 두 개면 됨
"""