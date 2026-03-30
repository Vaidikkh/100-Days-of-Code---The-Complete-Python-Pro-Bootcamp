import random
#import my_dic

#random_integer = random.randint(1,10 )
#print(random_integer)
#print(my_dic.my_fav_no)
#random_float0_1 = random.random() * 10  # it will generate the value b\w 0 to 1  if we multiply it with 10 then it will generate 1 to 10
#print(random_float0_1)
#random_float = random.uniform(1,10)
#print(random_float)
random_coin = random.randint(0,1)
print(random_coin)
if random_coin == 0:
    print("heads")
else :
    print("tails")