# Original file is located at https://colab.research.google.com/drive/19PyZ3X7ct2Levj5V39DEKY5S8W-qxf_W

ref_string = [1,2,3,4,1,2,3,1]
frame_size = 3

frame = []

page_fault = 0
page_hit = 0

for ref in ref_string:
  # checking page miss
  if ref in frame:
    page_hit += 1
  # checking empty space
  else:
    if len(frame) < frame_size:
      frame.append(ref)
    else:
      frame[page_fault % frame_size] = ref
    page_fault+=1

print(frame)
print("Page Hit: ", page_hit)
print("Page Fault: ", page_fault)
