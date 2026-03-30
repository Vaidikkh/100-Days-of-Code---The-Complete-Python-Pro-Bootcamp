def format_name(f_name,l_name):
    if f_name =="" or l_name =="":
        return  "You did not provide the inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}" # the return comes in functoion means that it is the end of the function if therer is any code after return than that's not gonna execute
    # print("hii") # this code is unreachable

print(format_name(input("What's your First name?"), input("What's your last name?")))
"""
def function_1(text):
    return text +text

def function_2(text):
    return text.title()

op = function_2(function_1("helLo"))
print(op)"""


