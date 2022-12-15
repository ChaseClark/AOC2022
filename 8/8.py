with open("./8/input.txt") as f:
    lines = f.read().strip().split('\n')
# print(lines)

# l = len(lines)
# w = len(lines[0])

# tree_map = {}

# print(f'processing {l} x {w} grid...')

# # loop through all inner rows and columns
# for r in range(l):

#     for c in range(w):
#         # check for perimiter nodes
#         if r == 0 or r == l - 1 or c == 0 or c == w - 1:
#             tree_map[(r,c)] = True
#             # stop processing further
#             continue
#         else:
#             tree_map[(r,c)] = False
#         height = int(lines[r][c])
        
#         # # check left
#         west_list = []
#         for i in lines[r][0:c]:
#             n = int(i)
#             west_list.append(n)

#         if max(west_list) < height:
#             tree_map[(r,c)] = True


#         # # print(lines[r][c+1:w])
#         # # right
#         east_list = []
#         for i in lines[r][c+1:w]:
#             n = int(i)
#             east_list.append(n)

#         if max(east_list) < height:
#             tree_map[(r,c)] = True

#         # # north
#         north_list = []
#         for i in range(r):
#             n = int(lines[i][c])
#             north_list.append(n)
#         if max(north_list) < height:
#             tree_map[(r,c)] = True

#         # south
#         south_list = []
#         for i in range(r+1,l):
#             n = int(lines[i][c])
#             south_list.append(n)
#         if max(south_list) < height:
#             tree_map[(r,c)] = True


#         # for each node we need to check north south east west and 
#         # make sure each number in that direction is lower than current


# total_visible = len([t for t in tree_map.values() if t == True])
# print(total_visible)


# part 2 


l = len(lines)
w = len(lines[0])

tree_map = {}

print(f'processing {l} x {w} grid...')

# loop through all inner rows and columns
for r in range(l):

    for c in range(w):
        # check for perimiter nodes
        if r == 0 or r == l - 1 or c == 0 or c == w - 1:
            tree_map[(r,c)] = 1
            # stop processing further
            continue
        else:
            tree_map[(r,c)] = 1
        height = int(lines[r][c])
        
        # check left
        west_list = []
        for i in reversed(lines[r][0:c]):
            n = int(i)
            if n < height:
                west_list.append(n)
            else:
                west_list.append(n)
                break

        # count how many in a row are less and multiple total by the count
        if len(west_list) > 1:
            tree_map[(r,c)] *= len(west_list)

        # right
        east_list = []
        for i in lines[r][c+1:w]:
            n = int(i)
            if n < height:
                east_list.append(n)
            else:
                east_list.append(n)
                break

        if len(east_list) > 1:
            tree_map[(r,c)] *= len(east_list)

        # north
        north_list = []
        for i in range(r-1,-1,-1):
            n = int(lines[i][c])
            if n < height:
                north_list.append(n)
            else:
                north_list.append(n)
                break
        
        if len(north_list) > 1:
            tree_map[(r,c)] *= len(north_list)

        # south
        south_list = []
        for i in range(r+1,l):
            n = int(lines[i][c])
            if n < height:
                south_list.append(n)
            else:
                south_list.append(n) # blocked
                break

        if len(south_list) > 1:
            tree_map[(r,c)] *= len(south_list)



# total_visible = len([t for t in tree_map.values() if t == True])
# print(total_visible)

best_view = max(tree_map.values())
for key in tree_map.keys():
    print(key,tree_map[key])

print(best_view)