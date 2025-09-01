# ccazzzzbb, kin 같이 단어 내 모든 문자에 대해서, 각 문자가 연속해서 나타나는 그룹 단어 찾기

n = int(input())

cnt = 0
slice_word = ""

for i in range (n):
  word = input()
  is_groupword = True

  for j in range(len(word)-1): # 마지막 문자 전까지
    if word[j] != word[j+1]: # 현재 인덱스의 문자와 다음 인덱스의 문자가 다를 때
      slice_word = word[j+1:] # 다음 인덱스부터 마지막까지 슬라이싱
      
      if slice_word.count(word[j]) > 0: # 현재 문자가 슬라이싱한 문자열에 포함돼있다면
        is_groupword = False # 그룹 단어 아님

  if is_groupword: # True면 그룹 단어
    cnt += 1

print(cnt)