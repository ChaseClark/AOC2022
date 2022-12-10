# with open("./10/input2.txt") as f:
#     lines = f.read().strip().split('\n')

# program = []

# class operation:
#     def __init__(self,name,amount = None, lifetime = 1) -> None:
#         self.name = name
#         self.amount = amount
#         self.lifetime = lifetime

#         if amount:
#             self.amount = int(self.amount)

#     def __str__(self) -> str:
#         return f'{self.name} {self.amount if self.amount else ""}'

# class computer:
#     clock_cycle = 0
#     x_register = 1
#     important_cycles = [20,60,100,140,180,220]
#     stack = []
#     signal_total = 0
#     crt_width=40
#     crt_height=6
#     crt :list

#     def __init__(self) -> None:
#         # init the crt screen
#         self.crt = ['' for x in range(self.crt_width * self.crt_height)]
#         print(len(self.crt))

#     def process(self, op: operation = None) -> None:
#         while len(self.stack) > 0:
#             self.clock_cycle+=1

#             if self.clock_cycle in self.important_cycles:
#                 self.signal_total += self.clock_cycle * self.x_register

#             if self.stack[-1].lifetime > 1:
#                 self.stack[-1].lifetime -= 1
#             else:
#                 op = self.stack.pop()
#                 if op.name == 'addx':
#                     self.x_register += op.amount

#             print(f'|{self.clock_cycle}| {op}\tx={self.x_register}\t tot:{self.signal_total}')


# for line in lines:
#     temp = line.split(' ')
#     if len(temp) < 2:
#         program.append(operation(temp[0]))
#     else:
#          program.append(operation(temp[0],int(temp[1]),2))


# c = computer()
# c.stack = list(reversed(program))
# c.process()
# # print(c.stack)
# # for el in c.stack:
# #     print(el)

# # for op in program:
# #     c.process(op)
# #     if c.clock_cycle in c.important_cycles:
# #         print(f'result: {c.x_register * c.clock_cycle}')


# print(c.signal_total)
# print('fin')

# part 2

with open("./10/input.txt") as f:
    lines = f.read().strip().split('\n')

program = []

class operation:
    def __init__(self,name,amount = None, lifetime = 1) -> None:
        self.name = name
        self.amount = amount
        self.lifetime = lifetime

        if amount:
            self.amount = int(self.amount)

    def __str__(self) -> str:
        return f'{self.name} {self.amount if self.amount else ""}'

class computer:
    clock_cycle = 0
    x_register = 1
    stack = []
    signal_total = 0
    crt_width=40
    crt_height=6
    crt_cycle= 0
    crt :list

    def __init__(self) -> None:
        # init the crt screen
        self.crt = ['' for x in range(self.crt_width * self.crt_height)]


    def process(self, op: operation = None) -> None:
        while len(self.stack) > 0:
            # decide what to draw to crt
            if self.crt_cycle in range(self.x_register -1, self.x_register+2):
                self.crt[self.clock_cycle] = '#'
            else:
                self.crt[self.clock_cycle] = '.'

            self.clock_cycle+=1
            
            if (self.crt_cycle + 1) % 40 == 0:
                self.crt_cycle = 0
            else:
                self.crt_cycle += 1


            if self.stack[-1].lifetime > 1:
                self.stack[-1].lifetime -= 1
            else:
                op = self.stack.pop()
                if op.name == 'addx':
                    self.x_register += op.amount


            # print(f'|{self.clock_cycle}| {op}\tx={self.x_register}\t tot:{self.signal_total}')
    
    def draw_crt(self) -> None:
        for i in range(len(self.crt)):
            print(self.crt[i], end='')
            if (i + 1) % 40 == 0:
                print('\n')
        print()


for line in lines:
    temp = line.split(' ')
    if len(temp) < 2:
        program.append(operation(temp[0]))
    else:
         program.append(operation(temp[0],int(temp[1]),2))


c = computer()
c.stack = list(reversed(program))
c.process()

c.draw_crt()
print('fin')