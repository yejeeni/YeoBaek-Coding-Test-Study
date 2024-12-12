# [수 찾기]

# N_array의 요소가 M_array에 있는지 확인
def solution(N_array, M_array):
    N_set = set(N_array)
    
    for m in M_array:
        if m in N_set:
            print("1")
        else :
            print("0")

# 처음 입력 받은 값은 리스트의 길이
# 두번 째로 입력 받은 값은 리스트의 요소 
N_num = int(input())
N_array = input().split()

M_num = int(input())
M_array = input().split()

solution(N_array, M_array)