def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            answer = i + 1  
        else:
            break  

    return answer


# def solution(citations):
#     citations.sort(reverse=True)  # 내림차순 정렬
#     h_index = 0  

#     for i, citation in enumerate(citations, start=1):  
#         if citation >= i:  # 현재 논문이 i번 이상 인용되었는가?
#             h_index = i  # h_index 업데이트
#         else:
#             break  # 더 이상 조건을 만족하지 않으면 종료

#     return h_index