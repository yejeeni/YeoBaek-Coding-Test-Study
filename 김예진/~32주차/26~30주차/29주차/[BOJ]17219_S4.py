# 두번째 줄부터 n개 줄에 걸쳐 주소, 비밀번호가 공백으로 구분되어 한 줄에 하나씩 입력
# n+2줄부터 m개 줄에 걸쳐 비밀번호를 찾으려는 주소가 한 줄에 하나씩 입력

import sys

n, m = map(int, sys.stdin.readline().split())

# address = []
# password = []

ad_pw = dict()

for _ in range(n):
    ad, pw = map(str, sys.stdin.readline().split()) # split() : 리스트 반환
    ad_pw[ad] = pw

    # address.append(ad)
    # password.append(pw)

for _ in range(m):
    search_ad = sys.stdin.readline().strip() # strip() : 문자열 반환

    print(ad_pw[search_ad])
        # print(search_ad, "==", address[i], "?")
        # if address[i] == search_ad:
        #     print(password[i])