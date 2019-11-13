from SaturatedNumber import SaturatedNumber

# | SRPNStack()
# |---------------------------------------------------------
# | A stack created which holds a set of SaturatedNumbers.
# |----------------------------------------------------
class SRPNStack:

    def __init__(self, saturation):

        self.saturation = saturation
        self.stack = []

    # | push()
    # |---------------------------------------------------------
    # | Creates a SaturatedNumber() out of the value passed
    # | as a parameter and pushes this onto the stack.
    # |-----------------------------------------
    def push(self, value):
        number = SaturatedNumber(self.saturation, value)

        self.stack.append(number)

    # | pop()
    # |----------------------------------------
    # | Removes and returns the value of the
    # | top SaturatedNumber on the stack.
    # |------------------------------
    def pop(self):
        return self.stack.pop().getValue()

    # | peek()
    # |----------------------------------------------------
    # | Returns the value of either the top item on the
    # | stack, or the value specified by the index.
    # |-----------------------------------------
    def peek(self, index=0):
        return self.stack[-1 - index].getValue()
