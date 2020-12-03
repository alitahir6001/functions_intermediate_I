import random


def randInt(min= 0, max= 100):
    num = random.random() * 100 - 32
    return int(num) # added 'int' to get rid of the decimal points, but if i don't have any operators on the line above (ex: random.random() * 20+15 ), it returns all 0's. 

print(randInt())                    # should print a random integer between 0 to 100
print(randInt(max=20))              # should print a random integer between 0 to 50
print(randInt(min=72))              # should print a random integer between 50 to 100
print(randInt(min=50, max=500))     # should print a random integer between 50 and 500

# this assignment was a little confusing -- I wasn't exactly sure what the end-goal of the assignment looked like (up to this point, all the assignments have been pretty clear about what to do, you just figure out how to do it). I had to reach out to a TA and be like "what the heck am i supposed to do with the provided code block?" and ended up going down a rabbit hole of different things to try...