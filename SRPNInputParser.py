from SRPNStack import SRPNStack

class SRPNInputParser:
    # | Contructor
    def __init__(self):
        self.stack = SRPNStack(100)

        self.operations = {"+" : self.add, "-" : self.subtract, "=" : self.equals}

    def parse(self, userInput):
        inputList = userInput.split(" ")

        for item in inputList:
            if item in self.operations:
                self.operations[item]()
            else:
                self.stack.push(int(item))

    def add(self):
        self.stack.push(self.stack.pop() + self.stack.pop())

    def subtract(self):
        self.stack.push(self.stack.pop() - self.stack.pop())

    def equals(self):
        number = self.stack.pop()
        print(number)
        self.stack.push(number)