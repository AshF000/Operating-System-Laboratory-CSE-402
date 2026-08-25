process = [
    ["p1", 0, 7],
    ["p2", 1, 4],
    ["p3", 2, 15],
    ["p4", 3, 11],
    ["p5", 4, 20],
    ["p6", 4, 9],
]

curr_time = 0
total_tat = 0
total_wt = 0

gantt = []
ready = []
result = []

time_quant = 5

original_burst = {p[0]: p[2] for p in process}

process.sort(key=lambda x: x[1])

while process or gantt:

    if not gantt:
        curr_time = max(curr_time, process[0][1])

    ready = [p for p in process if p[1] <= curr_time]

    for p in ready:
        gantt.append(p)
        process.remove(p)

    curr_p = gantt.pop(0)

    if curr_p[2] > time_quant:
        curr_time += time_quant
        curr_p[2] -= time_quant

        ready = [p for p in process if p[1] <= curr_time]

        for p in ready:
            gantt.append(p)
            process.remove(p)

        gantt.append(curr_p)

    else:
        curr_time += curr_p[2]

        ct = curr_time
        tat = ct - curr_p[1]
        wt = tat - original_burst[curr_p[0]]

        total_tat += tat
        total_wt += wt

        result.append([
            curr_p[0],
            curr_p[1],
            original_burst[curr_p[0]],
            ct,
            tat,
            wt
        ])

result.sort()

print("Process\tAT\tBT\tCT\tTAT\tWT")

for r in result:
    print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}")

print("\nAverage TAT =", total_tat / len(result))
print("Average WT  =", total_wt / len(result))
