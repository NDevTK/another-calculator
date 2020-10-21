import re

#Example:  number.number + number.number
# 0.1 + 0.2 = 0.30000000000000004

parts = re.compile(r'([0-9.]*)([+*-/][0-9.]*)')

def badParser(user_input):
    # Remove spaces from user_input
    user_input = user_input.replace(" ", "")
    state = False
    # Regular expression... sorry
    for (group1, change) in re.findall(parts, user_input):
        if(state == False):
            # Set Initial number
            state = getNumber(group1)
        state = parseChange(state, change)
    return getNumber(state)

def parseChange(state, change):
    # action can be + - * /
    action = change[0]
    # remove action from change
    number2 = getNumber(change[1:])
    if(action == "*"):
        return state * number2
    if(action == "+"):
        return state + number2
    if(action == "/"):
        if(number2 == 0):
            print("ERROR: Cannot divide by 0")
            return state
        return state / number2
    if(action == "-"):
        return state - number2
    
def getNumber(string):
    #Float or int (Its a mess)
    if "." in str(string):
        try:
            return float(string)
        except ValueError:
            return 0
    else:
        try:
            return int(string)
        except ValueError:
            return 0

def header():
    print("A Calculator\nActions: * + - /")

header()
while True:
    user_input = input("Question: ")
    answer = badParser(user_input)
    print(answer)
