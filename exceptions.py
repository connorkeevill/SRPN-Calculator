
# | StackOverflow()
# |--------------------------------------
# | The exception to be raised in the
# | event of a stack overflow.
# |-----------------------
class StackOverflowException(Exception):

    def __init__(self):
        self.message = "Stack overflow."

# | StackUnderflow()
# |-------------------------------------
# | The exception to be raised in the
# | event of a stack underflow.
# |-----------------------
class StackUnderflowException(Exception):

    def __init__(self):
        self.message = "Stack underflow."

# | StackEmptyException()
# |--------------------------------------------
# | The exception that is raised in the event
# | that the stack's peeked at while empty.
# |--------------------------------------
class StackEmptyException(Exception):

    def __init__(self):
        self.message = "Stack empty."
