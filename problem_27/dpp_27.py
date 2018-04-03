def check_complete(bracket_string):
    bracket_q = list()
    for i in range(len(bracket_string)):
        if is_open(bracket_string[i]):
            bracket_q.insert(0,bracket_string[i])
        else:
            if len(bracket_q)<=0:
                return False
            check_bracket = bracket_q.pop(0)
            if not is_compliment(bracket_string[i], check_bracket):
                return False
    if len(bracket_q)>0:
        return False
    return True

def is_open(bracket):
    list_open = ["(", "[", "{"]
    if bracket in list_open:
        return True
    return False

def is_compliment(bracket_1, bracket_2):
    list_pairs = [["(",")"],["{","}"],["[","]"]]
    for i in list_pairs:
        if bracket_1 in i and bracket_2 in i:
            return True
    return False


test_cases = ["([])[]({})","((()","([)]", "}{"]

for i in test_cases:
    print(check_complete(i))
