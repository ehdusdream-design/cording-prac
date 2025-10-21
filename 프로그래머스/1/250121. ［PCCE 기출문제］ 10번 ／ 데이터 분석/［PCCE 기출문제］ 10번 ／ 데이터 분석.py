def solution(data, ext, val_ext, sort_by):
    # 컬럼 이름 → 인덱스 매핑
    value = ["code", "date", "maximum", "remain"]
    ext_index = value.index(ext)
    sort_index = value.index(sort_by)

    # 조건 만족하는 데이터만 뽑기
    filtered = [row for row in data if row[ext_index] < val_ext]

    # 정렬
    filtered.sort(key=lambda x: x[sort_index])
    return filtered
