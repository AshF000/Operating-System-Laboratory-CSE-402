process = [
    ["p1", 3, 5],
    ["p2", 2, 2],
    ["p3", 3, 3],
    ["p4", 6, 4],
    ["p5", 2, 9],
    ["p6", 1, 5],
]

curr_time = 0
total_tat = 0
total_wt = 0
time_quant = 1

result = []
p_len = len(process)

toschedule = [
    [p[0], p[1], p[2], p[2]]
    for p in process
]

while toschedule:

    available = [p for p in toschedule if p[1] <= curr_time]

    if not available:
        curr_time = min(p[1] for p in toschedule)
        continue

    available.sort(key=lambda x: x[3])

    curr_p = available[0]

    curr_p[3] -= time_quant
    curr_time += time_quant

    if curr_p[3] <= 0:

        ct = curr_time
        tat = ct - curr_p[1]
        wt = tat - curr_p[2]

        total_tat += tat
        total_wt += wt

        result.append([
            curr_p[0],
            curr_p[1],
            curr_p[2],
            ct,
            tat,
            wt
        ])

        toschedule.remove(curr_p)


print("Preemptive:")
print("P_ID\tAT\tBT\tCT\tTAT\tWT")

for p in result:
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\t{p[5]}")

print("Average TAT:", total_tat / p_len)
print("Average WT:", total_wt / p_len)
