from SaturatedNumber import SaturatedNumber
from exceptions import StackOverflowException, StackUnderflowException, StackEmptyException

# | SRPNStack()
# |---------------------------------------------------------
# | A stack created which holds a set of SaturatedNumbers.
# |----------------------------------------------------
class SRPNStack:

    def __init__(self, saturation):

        self.saturation = saturation
        self.stack = []

        # | As defined by legacy system, there is a stack limit of 23
        self.stackLimit = 23

    # | push()
    # |-------------------------------------------------------------
    # | Checks that there is still space on the stack, raising
    # | StackOverflowException if not, creates a new
    # | SaturatedNumber() based on the value
    # | parameter, and pushes this
    # | onto the stack.
    # |----------
    def push(self, value):
        # | If we've reached the stack limit, raise a StackOverflowException
        if len(self.stack) >= self.stackLimit:
            raise StackOverflowException
        # | Otherwise just push onto the stack
        else:
            number = SaturatedNumber(self.saturation, value)
            self.stack.append(number)

    # | pop()
    # |---------------------------------------------------------------
    # | Checks that there are enough items on the stack, raising
    # | a StackUnderflowException if not, and returns either
    # | the value of the top item, or the value of the
    # | item specified by the index given, and
    # | removes that item from the stack.
    # |-----------------------------
    def pop(self, index=0):
        # | If there are no items in the stack when trying to pop, raise a StackUnderflowException.
        if len(self.stack) - index <= 0:
            raise StackUnderflowException()
        # | Otherwise, pop the top item off the stack.
        else:
            return self.stack.pop(-1 - index).getValue()

    # | peek()
    # |----------------------------------------------------
    # | Returns the value of either the top item on the
    # | stack, or the value specified by the index.
    # |-----------------------------------------
    def peek(self, index=0):
        # | If trying to peek at an empty stack, raise a StackEmptyException
        if len(self.stack) == 0:
            raise StackEmptyException

        if index > len(self.stack):
            raise IndexError

        # | We do [-1 - index] as this let's an index of, say, 4 to be
        # | passed, getting the 4th item from the top of the stack.
        return self.stack[-1 - index].getValue()

    # | count()
    # |--------------------------------------------
    # | Returns the number of items on the stack.
    # |----------------------------------------
    def count(self):
        return len(self.stack)
