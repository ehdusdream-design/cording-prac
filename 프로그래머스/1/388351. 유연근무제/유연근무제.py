def solution(schedules, timelogs, startday):
    day = 0
    count = 0
    def day_check(start, index):
        return (start-1+index)%7+1
    
    def overtime(n):
        if n%100 >= 60:
            return (n//100+n%100//60)*100+n%100%60
        else:
            return n
    
    for i in range(len(timelogs)):
        day = 0
        for j in range(7):
            check = day_check(startday, j)
            if check in (6,7):
                continue
            if timelogs[i][j] <= overtime(schedules[i]+10):
                day += 1
        if day == 5:
            count += 1
                
    return count