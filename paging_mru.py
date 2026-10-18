# Original file is located at   https://colab.research.google.com/drive/1al3-70qnNTj6PEIog_IG42AOFQQHlKm2

print("Name: Ashfiqul Islam Afnan")
print("Reg: 23101106")
print("Algo: MRU (Paging)")
print()
ref_string = [7,0,1,2,0,3,0,4,2,3]
frame_size = 4

frame = []

page_hit = 0
page_fault = 0
recent = ref_string[frame_size-1]

for ref in ref_string:
  if ref in frame:
    page_hit += 1
    recent = ref
  else:
    if len(frame) < frame_size:
      frame.append(ref)
    else:
      frame[frame.index(recent)] = ref
    recent = ref
    page_fault +=1

print(frame)
print("page hit:", page_hit)
print("page fault:", page_fault)
