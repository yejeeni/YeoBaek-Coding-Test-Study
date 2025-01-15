def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}  # 신고된 횟수 저장된 딕셔너리
    #print(set(report))
    #print(answer)

    for r in set(report):  #--> set을 통해 동일한 report를 제거
        reports[r.split()[1]] += 1  # report의 뒷값인 reports에 1추가
    #print(reports)

    for r in set(report):
        if reports[r.split()[1]] >= k:   # 횟수를 k랑 비교해서 크면
                   #id_list에 있는 r 앞값(신고자)의 순번에 1추가
            answer[id_list.index(r.split()[0])] += 1

            
    #시간복잡도 O(n*m)  마지막에 index가 비효율적임
    return answer


    """answer = [0] * len(id_list)
    report_dic = {}
    count_dic = {}
    out_list = []

    #딕셔너리 초기값 설정
    for id in id_list:
        report_dic[id] = set()
        count_dic[id] = 0
        
    #report를 정리 (report_dic)
    for r in report:
        a,b = r.split()
        report_dic[a].add(b)
    
    # 각 id별 신고받은 횟수 정리(count_dic)
    for key, value in report_dic.items():
        for v in value:
            count_dic[v] += 1

    #count된 값이 k 넘는 유저만 out_list에 추가
    for key, value in count_dic.items():
        if value >= k:
            out_list.append(key)        
    #print(out_list)
    
    #id_list대로 for문 돌려서 report_dic에 리스트로 저장된 value값을 for문 돌려서 각각 out_list에 있는지 확인하고 있으며 answer에 해당 순서를 1증가시켜줌
    #그러면 value에 있는 유저 중 정지된 유저 수만큼이 저장됨
    for i, key in enumerate(id_list):  # 인덱스, 내용값
        for rd in report_dic[key]:
            if rd in out_list:
                answer[i] += 1
        
    #print(report_dic)
    #print(count_dic)
    
    #시간복잡도 O(n+m)  //신고자수 + 신고수
    
    """
