print("FCFS - Disc Scheduling Algorithm")
head = 46
request_queue = [0, 13, 41, 50, 63, 89, 100]

total = 0
current = head

for r in request_queue:
    total += abs(current - r)
    current = r

print("Service Order:", request_queue)
print("Total Head Movement:", total)
