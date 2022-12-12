with open("./11/input2.txt") as f:
    lines = f.read().strip().split('\n\n')
# print(lines)

class monkey_test:
    def __init__(self,divisor: int, truth_monkey: int, false_monkey: int) -> None:
        self.divisor = divisor
        self.truth_monkey = truth_monkey
        self.false_monkey = false_monkey

    def __str__(self) -> str:
        return f'divisor:{self.divisor} tm:{self.truth_monkey} fm{self.false_monkey}'


class monkey:
    inspection_count = 0

    def __init__(self,id: int, items: list, operation, test) -> None:
        self.id = id
        self.items = items
        self.operation = operation # use eval()
        self.test = test # maybe make this its own class?

    def __str__(self) -> str:
        return f'monkey:{self.id} items:{self.items} operation:{self.operation} test:{str(self.test)}'

    def inspect_items(self):
        if len(self.items) < 1:
            return
        print(f'Monkey {self.id}:')
        for item in self.items:
            print(f'Monkey inspects item with worry level of {item}:')
            old = item
            new = eval(self.operation)
            print(f'{self.operation} -> {new}')
            new = new // 3
            print(f'dividing worry by 3 -> {new}')
            test_passed = new % self.test.divisor == 0
            if test_passed:
                print(f'current worry level is divisible by {self.test.divisor}')
                print(f'item with worry level {new} is thrown to monkey {self.test.truth_monkey}')
                monkeys[self.test.truth_monkey].items.append(new)
                print(monkeys[self.test.false_monkey].items)

            else:
                print(f'current worry level is not divisible by {self.test.divisor}')
                print(f'item with worry level {new} is thrown to monkey {self.test.false_monkey}')
                monkeys[self.test.false_monkey].items.append(new)
                print(monkeys[self.test.false_monkey].items)


            self.inspection_count += 1

monkeys = {}

# parse text file into n monkey objects
for line in lines:
    # print(line)
    l = line.strip().split('\n')
    # print(l)
    id = int(l[0].strip(':').split(' ')[1])
    items = l[1].strip().replace(':','').replace(',','').split(' ')[2:] # gets n items in list
    items = [int(i) for i in items]
    operation = l[2].strip().split('=')[1].strip()
    divisor = int(l[3].strip().split(' ')[-1])
    truthy = int(l[4].strip().split(' ')[-1])
    falsey = int(l[5].strip().split(' ')[-1])

    mt = monkey_test(divisor,truthy,falsey)
    m = monkey(id,items,operation,mt)
    monkeys[m.id] = m
    # print(id,items,operation,divisor,truthy,falsey)
    # print(id)

rounds = 20
for key in monkeys.keys():
    # print(monkeys[key])
    monkeys[key].inspect_items()

# print()
# print(f'round |1|')
# for key in monkeys.keys():
#     # print(monkeys[key])
#     print(f'Monkey {key}: inspected items {monkeys[key].inspection_count} times.')

print()
print(f'round |1| the monkeys are holding keys with these worry levels:')
for key in monkeys.keys():
    # print(monkeys[key])
    print(f'Monkey {key}: {monkeys[key].items}')