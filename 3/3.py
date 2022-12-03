with open("./3/input.txt") as f:
    lines = f.read().split('\n')

# total = 0

# part 1

# for sack in lines:
#     length = len(sack)
#     left = sack[:length//2]
#     right = sack[length//2:length]
#     same = ''
#     for l in left:
#         for r in right:
#             if r==l:
#                 same = r

#     if same.islower():
#         total += ord(same)-96
#     elif same.isupper():
#         total += ord(same)-38
        
# print('---------------')
# print(f'total: {total}')

# part 2 
total = 0
running = True
index = 0

while running:
    if not len(lines)-3 >= index:
        running = False
        break

    one = lines[index]
    index+=1
    two = lines[index]
    index+=1
    three = lines[index]
    index+=1

    same = ''
    for o in one:
        for tw in two:
            for th in three:
                if th == o and th == tw:
                    same = th

    if same.islower():
        total += ord(same)-96
    elif same.isupper():
        total += ord(same)-38
        
print('---------------')
print(f'total: {total}')