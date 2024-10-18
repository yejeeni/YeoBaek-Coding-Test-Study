word = input().upper() # 입력 단어를 대문자로 변환

word_list = list(set(word)) # 입력 단어에서 중복된 문자를 제거하고 list로 변환

cnt = []
for i in word_list:
  cnt.append(word.count(i)) # 알파벳이 단어에 사용된 횟수를 count하여 cnt에 append

# 가장 많이 사용된 알파벳이 여러 개인지?
if cnt.count(max(cnt)) > 1:
  print("?")
else: # cnt에서 가장 큰 값(=가장 많이 사용된 알파벳)을 찾고, 해당 인덱스를 찾아서, 그 인덱스의 word_list 값을 출력
  print(word_list[cnt.index(max(cnt))])