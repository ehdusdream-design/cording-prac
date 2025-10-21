def solution(bandage, health, attacks):
    # 붕대: (연속 시전 시간, 초당 회복량, 추가 회복량)
    b_time, b_second, b_plus = bandage
    max_health = health            # 최대 체력 상한
    count = 0                      # 연속 시전 카운트

    # 공격 시간을 딕셔너리로: {시간: 피해량}
    attack_map = {t: d for t, d in attacks}
    last_time = attacks[-1][0]

    for t in range(1, last_time + 1):
        if t in attack_map:        # 이 초에 공격이 들어오면
            health -= attack_map[t]
            if health <= 0:        # 즉시 사망 판정
                return -1
            count = 0              # 연속 시전 끊김
        else:
            # 회복(초당)
            count += 1
            health += b_second

            # 연속 시전 보너스
            if count == b_time:
                health += b_plus
                count = 0

            # 최대 체력 넘지 않도록
            if health > max_health:
                health = max_health

    return health
