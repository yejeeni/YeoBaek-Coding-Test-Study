def solution(bandage, health, attacks):
    answer = 0
    attack_time = []
    damage = []
    max_health = health

    for i in range(len(attacks)):
        attack_time.append(attacks[i][0])
        damage.append(attacks[i][1])
    print(attack_time)

    skill_con = 0
    for t in range(1, attacks[-1][0]+1):
        if t in attack_time:
            health -= damage[attack_time.index(t)]
            skill_con = 0
        else:
            skill_con += 1
            health += bandage[1]
            if skill_con >= bandage[0]:
                skill_con = 0
                health += bandage[2]

        if health > max_health:
            health = max_health
        if health <= 0:
            answer = -1
            break
        answer = health
    return answer