box_size = [5, 1, 2, 3, 4]
box_size.sort()

i = 0
x = 1
while i + 1 < len(box_size):
    if box_size[i] == box_size[i + 1]:
        x = x + 1
    i = i + 1

print(box_size)
print(x)