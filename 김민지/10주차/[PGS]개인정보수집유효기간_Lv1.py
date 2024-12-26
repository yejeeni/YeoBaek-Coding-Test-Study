def solution(today, terms, privacies):
    answer = []
    #오늘 년월일 나누기
    t_year, t_month, t_day = map(int, today.split("."))
    
    #term를 딕셔너리로 표현
    term_dic = {}
    for term in terms:
        tt = term.split()
        term_dic.update({tt[0] : int(tt[1])})
        

    for number, privacy in enumerate(privacies, 1):
        a = privacy.split()
        t = a[1]
        year, month, day = map(int, a[0].split("."))
        
        term_months = term_dic[t]
        month += term_months
        
        while month > 12:
            month -= 12
            year += 1
        
        if (t_year > year) or (t_year == year and t_month > month) or (t_year == year and t_month == month and t_day >= day):
            answer.append(number)

    return answer