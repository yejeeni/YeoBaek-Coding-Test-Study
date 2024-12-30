while(True):
  leg_list = list(map(int, input().split()))
  if leg_list == [0, 0, 0]:
    break

  leg_list.sort()
  # 세 변의 길이가 삼각형의 조건을 만족하지 않는 경우
  if leg_list[2] >= leg_list[1] + leg_list[0]:
    print("Invalid")
  # 세 변의 길이가 모두 같은 경우
  elif leg_list[0] == leg_list[1] == leg_list[2]:
    print("Equilateral")
  # 두 변의 길이만 같은 경우
  elif leg_list[0] == leg_list[1] or leg_list[0] == leg_list[2] or leg_list[1] == leg_list[2]:
    print("Isosceles")
  # 세 변의 길이가 모두 다른 경우
  else:
    print("Scalene")