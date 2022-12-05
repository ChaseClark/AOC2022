with open("./4/input.txt") as f:
    lines = f.read().split('\n')

# print(lines)

total = 0

# for pair in lines:
#     elf1,elf2 = pair.split(',')

#     split1 = elf1.split('-')
#     split2 = elf2.split('-')

#     elf1_l = int(split1[0])
#     elf1_h = int(split1[1])

#     elf2_l = int(split2[0])
#     elf2_h = int(split2[1])

#     # print(elf1_l,elf1_h,elf2_l,elf2_h)
    
#     if (elf1_l <= elf2_l and elf1_h >= elf2_h) or (elf2_l <= elf1_l and elf2_h >= elf1_h):
#         total += 1

    
# print(f'total: {total}')
    

for pair in lines:
    elf1,elf2 = pair.split(',')

    split1 = elf1.split('-')
    split2 = elf2.split('-')

    elf1_l = int(split1[0])
    elf1_r = int(split1[1])

    elf2_l = int(split2[0])
    elf2_r = int(split2[1])

    # print(elf1_l,elf1_r,elf2_l,elf2_r)
    
    r1 = [*range(elf1_l,elf1_r+1,1)]
    r2 = [*range(elf2_l,elf2_r+1,1)]
    
    intersection = [value for value in r1 if value in r2]
    if len(intersection) > 0:
        total += 1

    
print(f'total: {total}')