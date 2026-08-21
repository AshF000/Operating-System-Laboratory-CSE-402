process = [
    ["p1", 3, 5],
    ["p2", 2, 2],
    ["p3", 3, 3],
    ["p4", 6, 4],
    ["p5", 2, 9],
    ["p6", 1, 5],
]

curr_time=0
total_tat=0
total_wt=0
queue = []
result=[]
p_len = len(process)

toschedule = sorted([list(p) for p in process], key=lambda x:x[1])

while toschedule or queue:

    if not queue and toschedule:
        curr_time = max(curr_time, toschedule[0][1])


    new = [p for p in toschedule if p[1] <= curr_time]
    for p in new:
        queue.append(p)

    toschedule = [p for p in toschedule if p not in new]

    if not queue and not toschedule:
        break

    queue.sort(key=lambda x:x[2])

    curr_p = queue.pop(0)

    completion_time = curr_time + curr_p[2]

    ct = completion_time
    tat = ct - curr_p[1]
    wt = tat - curr_p[2]

    total_tat += tat
    total_wt += wt

    result.append([curr_p[0], curr_p[1], curr_p[2], ct, tat, wt])

    curr_time = completion_time

print("Non-Preemptive:")
print("P_ID\tAT\tBT\tCT\tTAT\tWT")
for p in result:
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\t{p[5]}")
print("Average TAT:", total_tat / p_len)
print("Average WT:", total_wt / p_len)
