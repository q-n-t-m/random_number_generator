import itertools

my_permutation = itertools.permutations(range(7))

import random

my_random = [1,2,3,4,5,6,7]
random.shuffle(my_random)
my_random

random.choice([1,2,3,4,5])
random.choice(range(100))


# pick five numbers between 1 - 50 without repetition and 2 numbers between 1 - 12
#this function generates a euro million draw as two tuples (the 5 and the lucky stars)
def gen_euro_millions():
    euro_numbers = list(range(1,51))
    random.shuffle(euro_numbers)
    my_5 = euro_numbers[:5]

    lucky_stars_numbers = list(range(1,13))
    random.shuffle(lucky_stars_numbers)
    my_2 = lucky_stars_numbers[:2]

    my_5.sort()
    my_2.sort()

    return tuple(my_5), tuple(my_2)
