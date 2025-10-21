def solution(video_len, pos, op_start, op_end, commands):
    def to_seconds(time_str):
        mm, ss = map(int, time_str.split(":"))
        return mm*60 + ss

    def to_string(seconds):
        mm = seconds // 60
        ss = seconds % 60
        return f"{mm:02d}:{ss:02d}"

    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)

    for com in commands:
        # 실행 전 오프닝 체크
        if op_start <= pos <= op_end:
            pos = op_end

        # 명령 실행
        if com == "prev":
            pos = max(0, pos - 10)
        else:  # "next"
            pos = min(video_len, pos + 10)

        # 실행 후 오프닝 체크
        if op_start <= pos <= op_end:
            pos = op_end

    return to_string(pos)
