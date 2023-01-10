hour1,minute1,hour2,minute2 = input().split()

park_time = abs((int(hour2) - int(hour1))*60 + (int(minute2) - int(minute1)))
ans = 0
if park_time <= 15:
    print(ans)
elif park_time > 15 and park_time <= 180:
    while park_time > 0:
        ans += 10
        park_time -= 60
    print(ans)
elif park_time > 180 and park_time < 240:
    print(30)
elif park_time >=240 and park_time <= 360:
    while park_time >= 240:
        ans += 20
        park_time -= 60
    print(ans + 30)
elif park_time > 360:
    print(200)
