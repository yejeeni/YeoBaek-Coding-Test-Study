t = int(input()) # 테스트케이스 수

for i in range(t):
  n = int(input()) # 의상 수 
  wear_dict = {} # 의상종류: 의상이름 을 담을 딕셔너리

  for j in range(n):
    name, type = map(str, input().split()) # 이름, 종류

    # 딕셔너리의 값에 배열을 넣어서 종류별로 여러 개의 의상 이름을 저장
    if (type in wear_dict): # 딕셔너리에 이미 존재하는 종류일 경우
      wear_dict[type].append(name) # 해당 위치에 이름만 추가
    else: # 딕셔너리에 없는 종류일 경우
      wear_dict[type] = [name] # 새로 추가

  cnt = 1
  for k in wear_dict:
    # k는 의상 종류
    cnt *= (len(wear_dict[k])+1) # 안입는경우 때문에 +1

  print(cnt-1) # 모두 안입은 경우 -1