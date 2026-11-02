print("Preemptive - Priority Scheduling Algorithm")
process_list = [
    ["P1", 3, 4, 2],
    ["P2", 4, 2, 0],
    ["P3", 2, 6, 3],
    ["P4", 0, 3, 6],
    ["P5", 1, 2, 1]
]

n = len(process_list)

remaining = []

for p in process_list:
    remaining.append(p[2])

ct = [0] * n
time = 0
completed = 0

while completed < n:

    ready = []

    for i in range(n):
        if process_list[i][1] <= time and remaining[i] > 0:
            ready.append(i)

    if len(ready) == 0:
        time += 1
        continue

    ready.sort(key=lambda i: process_list[i][3])

    curr = ready[0]

    remaining[curr] -= 1
    time += 1

    if remaining[curr] == 0:
        ct[curr] = time
        completed += 1

total_tat = 0
total_wt = 0

print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")

for i in range(n):
    p = process_list[i]

    tat = ct[i] - p[1]
    wt = tat - p[2]

    total_tat += tat
    total_wt += wt

    print(p[0], "\t", p[1], "\t", p[2], "\t",
          p[3], "\t", ct[i], "\t", tat, "\t", wt)

print("\nAverage TAT:", total_tat / n)
print("Average WT:", total_wt / n)
