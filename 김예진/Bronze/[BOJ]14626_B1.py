isbn = input()
pos = isbn.index('*') # 훼손 숫자 인덱스

for num in range(10):
    total = 0
    for i in range(len(isbn)):
        if i == pos:
            n = num  
        else:
            n = int(isbn[i])
        
        if i % 2 == 0:
            total += n * 1
        else:
            total += n * 3
    
    if total % 10 == 0: 
        print(num)
        break