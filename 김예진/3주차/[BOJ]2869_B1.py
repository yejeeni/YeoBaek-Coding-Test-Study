# 땅 위의 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
# 달팽이는 낮에 A미터 올라가고, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

import math

a, b, v = map(int, input().split())

# 하루 등반 높이: a - b
# 오를 높이: v - b (낮에 정상에 도달하면 미끄러지지 않으므로 v가 아니라 v - b를 해줘야 함)
print(math.ceil((v - b)/(a - b)))