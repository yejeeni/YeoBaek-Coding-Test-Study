def solution(players, callings):  
    #처음에 이중for문으로 구현해 O(n^2)이였으나 런타임에러로 인해 
    #딕셔너리를 통해 O(n)으로 구현
    dic = {player: i for i, player in enumerate(players)}
    for call in callings:
        pos = dic[call]
        if pos > 0:
            pre = players[pos-1]
            players[pos - 1], players[pos] = players[pos], players[pos - 1]
        
        dic[call] -= 1
        dic[pre] += 1
    
    return players

"""
    for call in callings:
        for i in range(len(players)):
            if players[i] == call:
                temp = players[i-1]
                players[i-1] = players[i];
                players[i] = temp
"""