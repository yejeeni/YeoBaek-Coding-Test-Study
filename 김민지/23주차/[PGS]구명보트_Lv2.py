def solution(people, limit):
    people.sort()
    low, high = 0, len(people)-1   #가벼운 사람, 무거운 사람 위치정보
    boat = 0
    
    while low <= high: 
        if people[low] + people[high] <= limit: #무거운 사람 + 가벼운사람 < limit
            low += 1  
        high -= 1     
        boat += 1  
            
    return boat