data = []
total_list = []

with open("input.txt") as f:
    data = f.read().split('\n\n')

# create list of sub-lists from txt lines
for line in data:
    # print(int(line))
    total = 0
    for number in line.split('\n'):
        total += int(number)
    total_list.append(total)

total_list.sort(reverse=True)
print(sum(total_list[0:3]))