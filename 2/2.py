with open("./2/input.txt") as f:
    lines = f.read().split('\n')

# print(lines,len(lines))

ROCK = 1
PAPER = 2
SCISSORS = 3

score = 0

# part one

# for round in lines:
#     # print(round.split(' '))
#     choices = round.split(' ')
#     elf = choices[0]
#     player = choices[1]
#     player_normalized = ord(player)-23
#     result = player_normalized-ord(elf)
#     # this will assign a value for the match
#     # 1 or -2 means win (6 pts) , -1 or 2 means loss (0 pts), and 0 means tie (3pts)
#     # add the player choice to score, 1 for rock , 2 paper, 3 for scissors
#     round_score = 0
#     if result == 1 or result == -2:
#         round_score += 6
#     elif result == -1 or result == 2:
#         round_score += 0
#     elif result == 0:
#         round_score += 3

#     round_total = round_score + player_normalized-64 # add score for which shape you choose
#     # print(f'result:{result} -> choice:{player_normalized-64} + {round_score}={round_total}')
#     score += round_total


# part 2

for round in lines:
    choices = round.split(' ')
    elf = choices[0]
    outcome = choices[1]
    player = 0

    # now we need calculate the scored based on the desired outcome where
    #  X means you need to lose, Y means draw, and Z means you need to win

    round_score = 0

    win = 0

    if outcome == 'X':
        if elf == 'A':
            player = SCISSORS
        elif elf == 'B':
            player = ROCK
        elif elf == 'C':
            player = PAPER
        win = -1
    elif outcome == 'Y':
        player = ord(elf) - 64
    elif outcome == 'Z':
        if elf == 'A':
            player = PAPER
        elif elf == 'B':
            player = SCISSORS
        elif elf == 'C':
            player = ROCK
        win = 1

    if win > 0:
        round_score += 6
    elif win < 0:
        round_score += 0
    else:
        round_score += 3

    round_total = round_score + player
    score += round_total

print(score)