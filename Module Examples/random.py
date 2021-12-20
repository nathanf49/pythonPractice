import random

a = random.randint(1,100) # picks a random number between 1 and 100

b = random.randrange(0,100,5) # picks a random number in a range(start,step,step)

animals = ['cow', 'horse', 'chicken', 'alpaca', 'pig', 'goat', 'llama']
c = random.choice(animals) # picks a random list element

d = random.shuffle(animals) # shuffles indexes of elements in a list

e = random.sample(animals,3) # picks 3 items out of animals

