def pold(count, wallet, bill):
    if((wallet[0] >= bill[0]) & (wallet[1] >= bill[1]) |
      (wallet[0] >= bill[1]) & (wallet[1] >= bill[0])):
        return count
        
    if (bill[0] < bill[1]):
        bill[1] = bill[1] // 2
    else:
        bill[0] = bill[0] // 2
    count += 1

    print(bill, count)
    return pold(count, wallet, bill)

def solution(wallet, bill):
    count = 0

    answer = pold(count, wallet, bill)
    print(answer)

    return answer