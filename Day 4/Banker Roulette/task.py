import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#1
random_friend = random.randint(0, 4)
print(friends[random_friend])
#if random_friend == 0 :
#    print(friends[0])
#if random_friend == 1 :
#    print(friends[1])
#if random_friend == 2 :
#    print(friends[2])
#if random_friend == 3 :
#    print(friends[3])
#if random_friend == 4 :
#    print(friends[4])
#2
print(random.choice(friends))