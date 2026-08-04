process = [
    # [p_id, AT, BT]
    ["p1", 1, 1],
    ["p2", 2, 3],
    ["p3", 3, 3],
    ["p4", 5, 2]
]

# manual data input
# process=[]
# num_of_data = input("Enter number of processes:")

# for i in num_of_data:
#   p_id = input("Enter process id:")
#   AT = int(input("Enter arrival time:"))
#   BT = int(input("Enter burst time:"))
#   process.append([p_id, AT, BT])

process.sort(key=lambda x: x[1])

curr_time=0
total_tat = 0
total_wt = 0
for p in process:

  if curr_time < p[1]:
    curr_time = p[1]
    
  curr_time += p[2]
  
  CT = curr_time
  TAT = CT - p[1]
  WT = TAT - p[2]

  p.append(CT)
  p.append(TAT)
  p.append(WT)
  
  total_tat += p[4]
  total_wt += p[5]

avg_tat = total_tat/len(process)
avg_wt = total_wt/len(process)

print(f"Process:\nP_id-AT-BT-CT-TAT-WT")
for p in process:
    print(p)

print(f"\nAvg TAT: {avg_tat}")
print(f"Avg WT: {avg_wt}")
