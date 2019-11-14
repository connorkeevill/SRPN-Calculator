from SRPNStack import SRPNStack
from exceptions import StackOverflowException, StackUnderflowException, StackEmptyException

# | SRPNInputParser
# |------------------------------------------------------------------------
# | Essentially an interpreter for the inputs for the calculator. Input
# | can be given using the parse() function, which will handle the
# | data in the appropriate manner according to the calculator.
# |--------------------------------------------------------
class SRPNInputParser:

    def __init__(self):
        # | Create the stack using the saturation specified
        self.stack = SRPNStack(100)

        # | A dictionary that contains the set of all available operations
        # | and the corresponding methods to perform the operation.
        self.operations = {"+" : self.add, "-" : self.subtract, "*" : self.multiply, "/" : self.divide,
                           "^" : self.exponentiate, "%" : self.mod, "=" : self.equals}

    # | parse()
    # |--------------------------------------------
    # | Parses the input string as an RPN input.
    # |--------------------------------------
    def parse(self, inputString):
        # | Create a list out of the string, splitting on the spaces. This allows
        # | expressions like "3 3 + =" to be inputted without the need for
        # | splitting the separate elements onto different lines.
        inputList = inputString.split(" ")

        # | Iterate through the list
        for item in inputList:
            # | Either perform the operation.
            if item in self.operations:
                try:
                    self.operations[item]()
                except StackUnderflowException as e:
                    print(e.message)
            # | Or try to add the operand to the stack.
            else:
                # | Try-except block to catch a stack overflow.
                try:
                    self.stack.push(int(item))
                # | Output the error message in the event of a stack overflow.
                except StackOverflowException as e:
                    print(e.message)

    # | popOperands()
    # |-----------------------------------------------------------------------
    # | Try to pop the top two operands off of the stack and return them,
    # | them, handling the possible exception of a stack underflow.
    # |--------------------------------------------------------
    def popOperands(self):
        operand2 = self.stack.pop(1)
        operand1 = self.stack.pop()

        return operand1, operand2

    # | add()
    # |--------------------------------------------------
    # | Pops the top two items off the stack, adds them
    # | together and pushes the result back onto it.
    # |------------------------------------------
    def add(self):
        operand1, operand2 = self.popOperands()
        self.stack.push(operand1 + operand2)

    # | subtract()
    # |--------------------------------------------------------------------
    # | Pops the top two items off the stack, subtracts the top one from
    # | the one below it, and pushes the result back onto the stack.
    # |----------------------------------------------------------
    def subtract(self):
        operand1, operand2 = self.popOperands()
        self.stack.push(operand2 - operand1)

    # | multiply()
    # |--------------------------------------------
    # | Pops the top two items off the stack and
    # | pushes their product back onto it.
    # |--------------------------------
    def multiply(self):
        operand1, operand2 = self.popOperands()
        self.stack.push(operand1 * operand2)

    # | divide()
    # |----------------------------------------------------------------
    # | Pops the top two items off the stack and divides the second
    # | one by the top one, pushing the result back onto it.
    # |------------------------------------------------
    def divide(self):
        operand1, operand2 = self.popOperands()
        self.stack.push(operand2 / operand1)

    # | exponentiate()
    # |-----------------------------------------------------------------------
    # | Pops the top two items off the stack and raises the second one to
    # | the power of the first one, pushing the result back onto it.
    # |---------------------------------------------------------
    def exponentiate(self):
        operand1, operand2 = self.popOperands()
        self.stack.push(operand2 ** operand1)

    # | mod()
    # |-----------------------------------------------------------------
    # | Pops the top two items off the stack, mods the second one by
    # | the top one and pushes the result back onto the stack.
    # |-----------------------------------------------
    def mod(self):
        operand1, operand2 = self.popOperands()
        self.stack.push(operand2 % operand1)

    # | equals()
    # |-------------------------------------------------
    # | Prints the value of the top item on the stack.
    # |---------------------------------------------
    def equals(self):
        try:
            print(self.stack.peek())
        except StackEmptyException as e:
            print(e.message)
