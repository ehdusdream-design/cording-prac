def solution(wallet, bill):
    answer = 0

    min_wallet, max_wallet = sorted(wallet)
    bill.sort()

    while not (bill[0] <= min_wallet and bill[1] <= max_wallet):
        # 항상 큰 쪽만 반으로 줄인다
        bill[1] //= 2
        bill.sort()  # 다시 정렬해서 작은/큰 쪽 맞추기
        answer += 1

    return answer
