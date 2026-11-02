print("SSTF - Disc Scheduling Algorithm")
head = 46
request_queue = [0, 13, 41, 50, 63, 89, 100]

total = 0
current = head
order = []

while len(request_queue) > 0:

    closest = request_queue[0]

    for r in request_queue:
        if abs(current - r) < abs(current - closest):
            closest = r

    total += abs(current - closest)
    current = closest

    order.append(closest)
    request_queue.remove(closest)

print("Service Order:", order)
print("Total Head Movement:", total)
