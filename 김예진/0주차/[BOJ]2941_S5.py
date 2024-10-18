croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input = input()

croatia_cnt = 0
for i in croatia_alphabet:
  croatia_cnt += input.count(i) # 포함된 크로아티아 알파벳의 개수 총합

print(len(input) - croatia_cnt)
# 크로아티아 알파벳이 한 단어가 2자로 이루어져있으므로 문자열 전체 길이에서 크로아티아 알파벳 개수를 빼주면 단어 개수가 나옴