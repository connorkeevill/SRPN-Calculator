
# | SaturatedNumber()
# |--------------------------------------------
# | Class for a number which is saturated
class SaturatedNumber:

    def __init__(self, saturation, value=0):
        self.saturation = saturation

        self.value = 0
        self.setValue(value)

    # | setValue()
    # |----------------------------------------
    # | Set the value of the number, ensuring
    # | it stays within the saturated range
    # |----------------------------------
    def setValue(self, value):

        # | If the value is larger than the saturated value
        if value > self.saturation:
            self.value = self.saturation
        # | If smaller
        elif value < -self.saturation:
            self.value = -self.saturation
        # | If within range
        else:
            self.value = value

    # | getValue()
    # |------------------------------
    # | Returns the attribute value.
    # |--------------------------
    def getValue(self):
        return self.value
