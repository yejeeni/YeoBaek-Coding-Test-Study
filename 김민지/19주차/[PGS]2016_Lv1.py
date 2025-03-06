def solution(a, b):
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(1, a):  
        b += month[i]
    return week[(b+4)%7]