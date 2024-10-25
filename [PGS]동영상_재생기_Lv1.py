def solution(video_len, pos, op_start, op_end, commands):
    
    mm = int(pos[0:2])
    ss = int(pos[3:5])
    pos_s = mm * 60 + ss

    video_mm = int(video_len[0:2])
    video_ss = int(video_len[3:5])
    video_s = video_mm * 60 + video_ss

    s_mm = int(op_start[0:2])
    s_ss = int(op_start[3:5])
    ops_s = s_mm * 60 + s_ss
    
    e_mm = int(op_end[0:2])
    e_ss = int(op_end[3:5])
    ope_s = e_mm * 60 + e_ss
    
    if((pos_s >= ops_s)&(pos_s < ope_s)):
        pos_s = ope_s
    
    for command in commands:             
        if command == "prev":
            pos_s = pos_s - 10
            if (pos_s < 0):
                pos_s = 0

        elif command == "next":
            pos_s = pos_s + 10
            if(pos_s > video_s):
                pos_s = video_s
        
        if((pos_s >= ops_s)&(pos_s < ope_s)):
            pos_s = ope_s

        
    mm = str(pos_s // 60).zfill(2)
    ss = str(pos_s % 60).zfill(2)

    pos = mm + ":" + ss
    
    
    return pos