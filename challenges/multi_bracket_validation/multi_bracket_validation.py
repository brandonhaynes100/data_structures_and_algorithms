

# Your function should take a string as its only argument
# should return a boolean representing whether or not the
# brackets in the string are balanced. There are 3 types
# of brackets:
# Round Brackets : ()
# Square Brackets : []
# Curly Brackets : {}
def multi_bracket_validation(input_string):
    # if isinstance(input_string, str):
    #     raise TypeError

    openers_stack = list()

    for character in input_string:
        if character == '(' or character == '[' or character == '{':
            openers_stack.append(character)

        if character == ')':
            if len(openers_stack) < 1:
                return False
            temp = openers_stack.pop()
            if temp != '(':
                return False

        if character == ']':
            if len(openers_stack) < 1:
                return False
            temp = openers_stack.pop()
            if temp != '[':
                return False

        if character == '}':
            if len(openers_stack) < 1:
                return False
            temp = openers_stack.pop()
            if temp != '{':
                return False
    
    if len(openers_stack) > 0:
        return False
    
    return True
