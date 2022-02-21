"""Enumerate"""
l = ["chopstick", "momos", "cushion", "pillow"]
i = 1
# for item in l:
#     if i % 2==0:
#         print(item)
#     i += 1

for index,item in enumerate(l):
    if index%2==0:
        print(item)
