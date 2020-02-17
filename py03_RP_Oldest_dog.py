# Review Exercises (#1)

# Using the same Dog class, instantiate three new dogs, 
# each with a different age. Then write a function called, 
# get_biggest_number(), that takes any number of ages (*args) 
# and returns the oldest one. Then output the age of the 
# oldest dog like so:

# Output: The oldest dog is 7 years old.


class Dog:

    species = "Mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
romeo = Dog('Romeo', 5)
mike = Dog('Mike', 3)
spark = Dog('Spark', 4)

def get_biggest_number(*args):
    return max(args)

print(f'The oldest dog is {get_biggest_number(romeo.age, mike.age, spark.age)} years old.')






