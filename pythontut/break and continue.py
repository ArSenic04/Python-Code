"""Break and continue"""
i = 0
while i < 40:
    if i < 6:
        i = i + 1
        continue
    print(i, end=" ")
    if i == 23:
        break
    i = i + 1
