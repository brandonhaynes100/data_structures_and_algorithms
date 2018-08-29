

# Your function should take a string as its only argument
# should return a boolean representing whether or not the
# brackets in the string are balanced. There are 3 types
# of brackets:
# Round Brackets : ()
# Square Brackets : []
# Curly Brackets : {}
def multi_bracket_validation(input):
    if typeof(input) != 'string':
        raise Error
    
    openers_stack = list()

    for character in input:
        if character == '(' or character == '[' or character == '{':
            openers_stack.push(character)

        if character == ')':
            if len(openers_stack) < 1:
                return False
            if openers_stack.peek() != '(':
                return False
            if openers_stack.peek() == '(':
                openers_stack.pop()

        if character == ']':
            if len(openers_stack) < 1:
                return False
            if openers_stack.peek() != '[':
                return False
            if openers_stack.peek() == '[':
                openers_stack.pop()
                
        if character == '}':
            if len(openers_stack) < 1:
                return False
            if openers_stack.peek() != '}':
                return False
            if openers_stack.peek() == '}':
                openers_stack.pop()
    
    if len(openers_stack) > 0:
        return False
    
    return True
