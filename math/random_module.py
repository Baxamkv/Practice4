from random import *

lst = [6,8,4,9,7,5,1]

print(random()) #random float between [0,1)

print(randint(0,100)) #random integer between 0 and 100

shuffle(lst)

print(choice(lst)) #choose random one element