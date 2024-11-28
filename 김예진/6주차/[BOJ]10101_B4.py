angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

if (angle1 + angle2 + angle3) != 180:
  print("Error")
elif (angle1 == angle2 == angle3 == 60):
  print("Equilateral")
elif (angle1 == angle2) or (angle1 == angle3) or (angle2 == angle3):
  print("Isosceles")
else:
  print("Scalene")