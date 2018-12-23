
## . is single character
    ## Move one character over
## * matches zero or more
    ## Move until next characters match
def regular_exp_checker(string, reg_expression):
    string_pointer = 0
    expression_pointer = 0
    while expression_pointer > len(reg_expression)-1:
        ## If it's ".", move string pointer 1

        ## If it's "*", move string pointer until it points to thing after i

        ## If it's char, check match
