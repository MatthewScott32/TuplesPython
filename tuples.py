zoo = ("monkey", "chimp", "gorilla", "lion", "tiger", "bear", "wolf", "elephant", "cheetah", "human" )
print(zoo.index("gorilla"))

animal_in_zoo = "lion"
if animal_in_zoo in zoo:
    print(f'{animal_in_zoo} is in the zoo')

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, sevent_animal, eighth_animal, ninth_animal, tenth_animal) = zoo
print(tenth_animal)

new_zoo = list(zoo)

print(new_zoo)

new_zoo.extend(['panther'])
new_zoo.extend(['ardvark'])
new_zoo.extend(['dingo'])

new_new_zoo = tuple(new_zoo)
print(new_new_zoo)
