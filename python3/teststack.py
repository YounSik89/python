#module import from datastruct folder
from datastruct.Stack import *

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    
    if balanced and s.is_empty():
        return True
    else:
        return False

def par_checker2(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    
    if balanced and s.is_empty():
        return True
    else:
        return False
    
def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

def div_by_2(dec_num):
    rem_Stack = Stack()
    while dec_num > 0:
        rem = dec_num % 2
        rem_Stack.push(rem)
        dec_num = dec_num // 2
    bin_str = ""
    while not rem_Stack.is_empty():
        bin_str = bin_str + str(rem_Stack.pop())
    return bin_str

def base_converter(dec_num, base):
    digits = "0123456789ABCDEF"
    rem_Stack = Stack()
    while dec_num>0:
        rem = dec_num % base
        rem_Stack.push(rem)
        dec_num = dec_num // base
    new_str = ""
    while not rem_Stack.is_empty():
        new_str = new_str + digits[rem_Stack.pop()]
    return new_str



#print(par_checker('((()))'))
#print(par_checker("(()"))
#print(par_checker2('{{([][])}()}'))
#print(par_checker2('[{()]'))

#print(base_converter(25,2))
#print(base_converter(25,16))
#print(base_converter(25,3))
#print(div_by_2(42))

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()
    
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
                (prec[op_stack.peek()]>=prec[token]):
                    postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
            postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)

#print(infix_to_postfix("A * B + C * D"))
#print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
#print(infix_to_postfix("( A + B ) * ( C + D )"))

def postfix_to_infix(postfix_expr):
    prec = {}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()
    
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty() and 
                prec[op_stack.peek()]>=prec[token]):
                    postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
            postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("( A + B ) * ( C + D )"))

안녕하세요