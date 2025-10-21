def solution(players, callings):
    # 선수 이름 -> 현재 순위 매핑
    rank = {name: i for i, name in enumerate(players)}
    
    for call in callings:
        idx = rank[call]              # 현재 불린 선수의 순위
        be_player = players[idx-1]    # 앞에 있던 선수

        # 리스트 순위 바꾸기
        players[idx-1], players[idx] = players[idx], players[idx-1]

        # rank도 갱신하기
        rank[call] -= 1
        rank[be_player] += 1
    
    return players
