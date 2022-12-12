with open("./11/input2.txt") as f:
    lines = f.read().strip().split('\n')

class monkey:
    def __init__(self,id: int, items: list, operation: function, test) -> None:
        self.id = id
        self.items = items
        self.operation = operation # maybe make this its own class?
        self.test = test # maybe make this its own class?

    def __str__(self) -> str:
        pass

# parse text file into n monkey objects