from SRPNStack import SRPNStack
from exceptions import StackOverflowException, StackUnderflowException, StackEmptyException
import randomNumbers
import sys

# | SRPNInputParser
# |------------------------------------------------------------------------
# | Essentially an interpreter for the inputs for the calculator. Input
# | can be given using the parse() function, which will handle the
# | data in the appropriate manner according to the calculator.
# |--------------------------------------------------------
class SRPNInputParser:

    def __init__(self, saturation):
        # | Create the stack using the saturation specified
        self.stack = SRPNStack(saturation)

        # | A dictionary that contains the set of all available operations
        # | and the corresponding methods to perform the operation.
        self.operations = {"+" : self.add, "-" : self.subtract, "*" : self.multiply, "/" : self.divide,
                           "^" : self.exponentiate, "%" : self.mod, "=" : self.equals, "d" : self.d, "r" : self.r,
                           "£" : self.poundSign, "#" : self.comment}

        self.isCommenting = False

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

            # | If we're in the middle of a comment and the comment isn't ending, just skip this iteration
            if self.isCommenting and item != "#":
                continue

            # | If the item is an operation
            if item in self.operations:
                self.performOperation(item)

            # | If the item is an operand (i.e. just digit)
            elif item.isdigit():
                self.pushOperand(item)

            # | If we have operands that are 'stuck' to operators
            elif len(item) > 1:
                # | Make list out of the string, then put back into a string separated by spaces
                # | to allow it to be re-separated into a list in the next parse() call.
                splitItem = [character for character in item]
                splitItem = " ".join(splitItem)

                # | Re-parse the newly generated string
                self.parse(splitItem)

    # | pushOperand()
    # |------------------------------------------------------------------
    # | Pushes item passed as a parameter onto the stack, catching the
    # | exception that may be raised if the stack is already full.
    # |-------------------------------------------------------
    def pushOperand(self, item):
        # | The base in which the operand should be interpreted
        base = 10

        # | If the number is prefixed with a 0, it's to be considered an octal number
        if item[0] == '0':
            base = 8

        try:
            self.stack.push(int(item, base))
        except StackOverflowException as e:
            print(e.message)

    # | performOperation()
    # |--------------------------------------------------------------
    # | Tries to perform the operation passed as a parameter, but
    # | catches the exception of having no items on the stack.
    # |---------------------------------------------------
    def performOperation(self, operation):
        try:
            self.operations[operation]()
        except StackUnderflowException as e:
            print(e.message)

    # | popOperands()
    # |-----------------------------------------------------------------------
    # | Try to pop the top two operands off of the stack and return them,
    # | them, handling the possible exception of a stack underflow.
    # |--------------------------------------------------------
    def popOperands(self):
        # | We pop the second item off the stack before the first on. This
        # | means that any exceptions caused by a stack underflow will
        # | be raised before we've removed an item off the stack.
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
        self.pushOperand(operand1 + operand2)

    # | subtract()
    # |--------------------------------------------------------------------
    # | Pops the top two items off the stack, subtracts the top one from
    # | the one below it, and pushes the result back onto the stack.
    # |----------------------------------------------------------
    def subtract(self):
        operand1, operand2 = self.popOperands()
        self.pushOperand(operand2 - operand1)

    # | multiply()
    # |--------------------------------------------
    # | Pops the top two items off the stack and
    # | pushes their product back onto it.
    # |--------------------------------
    def multiply(self):
        operand1, operand2 = self.popOperands()
        self.pushOperand(operand1 * operand2)

    # | divide()
    # |----------------------------------------------------------------
    # | Pops the top two items off the stack and divides the second
    # | one by the top one, pushing the result back onto it.
    # |------------------------------------------------
    def divide(self):
        operand1, operand2 = self.popOperands()
        self.pushOperand(operand2 / operand1)

    # | exponentiate()
    # |-----------------------------------------------------------------------
    # | Pops the top two items off the stack and raises the second one to
    # | the power of the first one, pushing the result back onto it.
    # |---------------------------------------------------------
    def exponentiate(self):
        operand1, operand2 = self.popOperands()

        if operand1 < 0:
            print("Negative power.")
        else:
            self.pushOperand(operand2 ** operand1)

    # | mod()
    # |-----------------------------------------------------------------
    # | Pops the top two items off the stack, mods the second one by
    # | the top one and pushes the result back onto the stack.
    # |-----------------------------------------------
    def mod(self):
        operand1, operand2 = self.popOperands()
        self.pushOperand(operand2 % operand1)

    # | equals()
    # |-------------------------------------------------
    # | Prints the value of the top item on the stack.
    # |---------------------------------------------
    def equals(self):
        # | Try to peek at the top item, but catch the exception if the stack is empty.
        try:
            print(self.stack.peek())
        except StackEmptyException as e:
            print(e.message)

    # | d()
    # |-------------------------------------------------------
    # | The 'd' function. Prints the contents of the stack.
    # |-------------------------------------------------
    def d(self):
        # | Get the number of items in the stack
        items = self.stack.count()

        # | We iterate from 1 to items + 1 (instead of 0 to items) as this
        # | allows us to peek at the stack with the right index
        for i in range(1, items + 1):

            print(self.stack.peek(items - i))

    # | r()
    # |------------------------------------------------
    # | Pushes a random number to the stack based on
    # | GLIBC random number generator used by C.
    # |--------------------------------------
    def r(self):
        # | Get the random number an put it on the stack
        randomNumber = randomNumbers.numbers[randomNumbers.index]
        self.stack.push(randomNumber)

        # | Increment the index to move on the next number
        randomNumbers.index += 1

    # | poundSign()
    # |----------------------------------------------------
    # | The '£' function. Causes the calculator to exit.
    # |---------------------------------------------
    def poundSign(self):
        sys.exit()

    # | comment()
    # |---------------------------------------------------------------
    # | Allows comments to be inputted. Toggles the commenting flag.
    # |-----------------------------------------------------------
    def comment(self):
        self.isCommenting = not self.isCommenting

    # | unrecognisedInput()
    # |-----------------------------------------------------------
    # | Outputs a warning message should an input be erroneous.
    # |-----------------------------------------------------
    def unrecognisedInput(self, string):
        print("Unrecognised operator or operand \"" + string + "\".")


