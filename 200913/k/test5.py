def t_to_sec(t):
    t_split = [*map(int, t.split(':'))]

    return t_split[0] * 3600 + t_split[1] * 60 + t_split[2]

def sec_to_t(sec):
    t0 = sec // 3600
    t1 = (sec % 3600) // 60
    t2 = sec % 60

    return f'{t0:02}:{t1:02}:{t2:02}'

print(sec_to_t(999))
print(t_to_sec("99:59:59"))

def solution(play_time, adv_time, logs):
    if play_time == adv_time: return '00:00:00'

