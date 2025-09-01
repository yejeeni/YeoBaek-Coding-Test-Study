"""
길이가 짧은 것부터
길이가 같으면 사전 순으로
중복 제거
"""


n = int(input())
words = set() # 중복을 제거하기 위해 set 사용

for i in range(n):
  words.add(input())

words = list(words) # set은 순서가 없으니 list로

words.sort(key= lambda x : (len(x), x)) # 길이 순, 사전 순

for i in words:
  print(i)