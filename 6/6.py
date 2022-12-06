with open("./6/input.txt") as f:
    data = f.read().strip()
print(data)
# marker = 0
# # while loop to move length 4 packet across the input untill a unique packet is found

# index = 0

# while marker == 0:
#     packet = data[index:index+4]
#     print(packet,len(set(packet)) == len(packet))
#     if len(set(packet)) == len(packet):
#         marker = index + 4
#     index+=1
    
# print(marker)

# part 2 



marker = 0
# while loop to move length 4 packet across the input untill a unique packet is found

index = 0

while marker == 0:
    packet = data[index:index+14]
    print(packet,len(set(packet)) == len(packet))
    if len(set(packet)) == len(packet):
        marker = index + 14
    index+=1
    
print(marker)