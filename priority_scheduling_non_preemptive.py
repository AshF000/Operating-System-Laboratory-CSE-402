print("Non Preemptive - Priority Scheduling Algorithm")
process_list = [
    ["P1", 3, 4, 2],
    ["P2", 4, 2, 0],
    ["P3", 2, 6, 3],
    ["P4", 0, 3, 6],
    ["P5", 1, 2, 1]
]

n = len(process_list)
completed = []
time = 0

while len(completed) < n:

    ready = []

    for p in process_list:
        if p[1] <= time and p[0] not in completed:
            ready.append(p)

    if len(ready) == 0:
        time += 1
        continue

    ready.sort(key=lambda x: x[3])

    curr = ready[0]

    time += curr[2]
    curr.append(time)

    completed.append(curr[0])

total_tat = 0
total_wt = 0

print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")

for p in process_list:
    ct = p[4]
    tat = ct - p[1]
    wt = tat - p[2]

    total_tat += tat
    total_wt += wt

    print(p[0], "\t", p[1], "\t", p[2], "\t",
          p[3], "\t", ct, "\t", tat, "\t", wt)

print("\nAverage TAT:", total_tat / n)
print("Average WT:", total_wt / n)
