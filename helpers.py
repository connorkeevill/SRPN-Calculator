# | isNegativeNumber()
# |--------------------------------------------------
# | Returns a boolean indicating whether or not the
# | passed string's a number with a '-' in front.
# |--------------------------------------------
def isNegativeNumber(string):
    try:
        return string[0] == "-" and string[1:].isdigit()

    # | If the string happens to be empty, catch the index exception
    except IndexError as e:
        return False