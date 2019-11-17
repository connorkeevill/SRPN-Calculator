from SRPNInputParser import SRPNInputParser

saturation = 2147483647

# | Create the parser object
parser = SRPNInputParser(saturation)

# | Opening message
print("Use the calculator\n")

# | Main loop
while True:
    userInput = input()

    parser.parse(userInput)
