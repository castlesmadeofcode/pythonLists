import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))
# append a random number ranging from 1-6 to my_randoms list 10 times
# print(my_randoms)


# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False




    # Iterate your random number list here
    for randoms in my_randoms:
    # Does my_randoms contain number? Change the boolean.
        if randoms == number:
            the_numbers_match = True

    if the_numbers_match:
        print(f'{number} is in the random list')
    else:
        print(f'{number} is not the random list')
            
