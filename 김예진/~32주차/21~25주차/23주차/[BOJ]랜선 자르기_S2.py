# 이진탐색. 정렬된 리스트에서 검색 범위를 줄여나가며 값을 찾음

k, n = map(int, input().split()) # 기존 k개, 만들어야 하는 n개

lans = []
for _ in range(k):
  lans.append(int(input()))

start, end = 1, max(lans) # 가장 짧은 길이, 가장 긴 길이

while start <= end:
  mid = (start + end) // 2 # 이진탐색을 위한 랜선 길이 중간값

  lan_count = 0
  for i in lans:
    lan_count += i // mid # mid 길이의 선을 몇 개 만들 수 있는지 계산
  
  if lan_count >= n: # lan count가 만들어야하는 n보다 큰 경우
    start = mid + 1 # 랜선 최소 길이를 중간값 + 1로 설정
  else: # 작은 경우
    end = mid - 1 # 랜선 최대 길이를 중간값 - 1로 설정

print(end)