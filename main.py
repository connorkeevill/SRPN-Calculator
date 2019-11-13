from SRPNInputParser import SRPNInputParser

parser = SRPNInputParser()

print("Use the calculator\n")

while True:
    userInput = input()

    parser.parse(userInput)