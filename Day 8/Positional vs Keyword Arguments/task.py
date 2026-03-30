# Functions with input
'''
def greet_with_name(name, loc):
    print(f"Hello {name}")
    print(f"where is this place named {loc}?")


greet_with_name("Jack Bauer", "spiti") #positin  matches
greet_with_name(loc = "chitkul" , name = "vaidik")'''



def calculate_love_score(name1,name2):
    print(f"the first name is '{name1}'")
    print(f"the second name is '{name2}'")
    combined_name = name1 + name2
    lower_name = combined_name.lower()
    t = lower_name.count('t')
    r = lower_name.count('r')
    u = lower_name.count('u')
    e = lower_name.count('e')
    first = t+r+u+e
    l = lower_name.count('l')
    o = lower_name.count('o')
    v = lower_name.count('v')
    e = lower_name.count('e')
    second = l+o+v+e
    score = int(str(first)) + int(str(second))
    print(score)
calculate_love_score(" Kim Kardashian" , "Kanye West")