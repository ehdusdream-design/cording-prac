def solution(mats, park):
    # 가장 큰 돗자리부터 확인
    mats.sort(reverse=True)

    rows, cols = len(park), len(park[0])

    def can_place_mat(size):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                # size × size 영역을 모두 확인
                area_empty = all(
                    park[x][y] == "-1"
                    for x in range(i, i + size)
                    for y in range(j, j + size)
                )
                if area_empty:
                    return True
        return False

    for size in mats:
        if can_place_mat(size):
            return size

    return -1
