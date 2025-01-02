from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    wait_num = 0 #대기트럭 중 가장 앞 트럭이 truck_weights에서 몇번째인지
    bridge = deque()
    time = deque()
    total_weights = 0
    
    check = False
    while check == False:
        answer += 1 #시간 추가
        
        #시간이 지남에 따라 다리위의 트럭들이 건너야할 시간 줄이기
        for t in range(len(time)):
            time[t] -= 1
        
        if (wait_num != 0) and (time[0] == 0): #다리를 다 건넜다면 큐와 무게에서 제거
            time.popleft()
            run_weights = bridge.popleft()
            total_weights -= run_weights
            if (wait_num == len(truck_weights) and len(bridge) == 0): #마지막 트럭이 다리를 다 건넜다면 종료
                check = True
        
        #대기 중인 트럭이 없다면 그냥 다음으로
        if wait_num == len(truck_weights): 
            continue
        
        #다리에 트럭이 올라갈 수 있는지 확인    
        wait_weights = truck_weights[wait_num] #가장 앞 대기트럭 무게
        if (total_weights + wait_weights) <= weight:
            bridge.append(wait_weights)
            time.append(bridge_length)
            total_weights += wait_weights
            wait_num += 1
        
    return answer