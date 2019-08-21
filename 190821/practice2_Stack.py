def checkParenthesis(strinput):
    top = 0
    small = []
    medium = []
    large = []
    for char in strinput:
        if char == '(':
            small.append(1)
        elif char == '{':
            medium.append(1)
        elif char == '[':
            large.append(1)
        elif char == ')':
            
        elif char == '}':

        elif char == ']':
        
        else:
            continue
