from SRPNInputParser import SRPNInputParser

# | Create the parser object
parser = SRPNInputParser()

# | Opening message
print("Use the calculator\n")

# | Main loop
while True:
    userInput = input()

    parser.parse(userInput)