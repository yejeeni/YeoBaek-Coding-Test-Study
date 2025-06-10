"""
1. 좌표 [2, 4, -10, 4, -9] 가 들어온다
2. 좌표를 크기 순으로 [-10, -9, 2, 4, 4] 정렬하고, 증복을 제거하여 [-10, -9, 2, 4]로 만든다.
3. 이 배열을 인덱스로 치환한다. -10: 0, -9:, 1, 2:, 2, 4: 3 이 값을 원래 좌표에 적용하면 좌표압축의 결과가 된다.
4. 좌표 압축 결과 [2, 4, -10, 4, -9] -> [2, 3, 0, 3, 1]
"""
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr2 = sorted(set(arr)) 
# 리스트명.sort(): 리스트형의 메소드. 리스트의 원본 값을 직접 수정한다.
# sorted(리스트명): 내장 함수. 리스트 원본 값은 그대로이고, 정렬 값을 반환한다.

# dic = {'key' : 'value', ...}
dic = {}
for i in range(len(arr2)):
  dic[arr2[i]] = i
  """
  딕셔너리 컴프리헨션 (반복문을 딕셔너리 생성과 동시에 한 줄로 표현)
  {key: value for 요소 in 반복 가능한 객체}
  ex)   dic = {arr[i]: i for i in range(len(arr))}
        dic = {value: index for index, value in enumerate(arr2)}
  enumerate()는 리스트 같은 자료형의 요소를 반복하며 인덱스와 값을 동시에 갖고 올 수 있음
  """

for i in arr:
  print(dic[i], end=' ')