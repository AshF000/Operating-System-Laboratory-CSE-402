print("SCAN - Disc Scheduling Algorithm")
head = 46
request_queue = [0, 13, 41, 50, 63, 89, 100]

left = []
right = []

for r in request_queue:
    if r < head:
        left.append(r)
    else:
        right.append(r)

left.sort(reverse=True)
right.sort()

order = left + [0] + right

total = 0
current = head

for r in order:
    total += abs(current - r)
    current = r

print("Service Order:", order)
print("Total Head Movement:", total)
