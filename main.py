"""
1)Function: add_numbers
Write a Python function named add_numbers that takes two parameters num1 and num2, and returns the sum of the two numbers.
"""
def add_numbers(num1,num2):
    return num1 + num2

print(add_numbers(2,4))

"""
2)Function: is_even
Write a Python function named is_even that takes a single parameter number and returns True if the number is even, and False otherwise.
"""
def is_even(number):
    if number %2 ==0:
        return True
    else:
        return False
print(is_even(3))

"""
3)Function: reverse_string
Write a Python function named reverse_string that takes a string text as input and returns the reversed version of that string.
"""
def reverse_string (string):
    return string[::-1] #to reverse i have used the step index as -1 to slice in the reverse direction

print(reverse_string("moringa"))

"""
4)Function: count_vowels
Write a Python function named count_vowels that takes a string text as input and returns the count of vowels (a, e, i, o, u) in the string. Ignore case sensitivity.
"""
def count_vowels(string):
    input_texts=string.lower()
    vowels="aeiou"
    return sum(1 for letter in input_texts if letter in vowels) #if letter is a vowel it returns a 1 which is added to the total sum 
print(count_vowels("moringa school"))

"""
5)Function: calculate_factorial
Write a Python function named calculate_factorial that takes a non-negative integer n as input and returns the factorial of that number. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
"""
def calculate_factorial(number):
    if number < 0:
        return "Please enter a positive integer"
    
    factorial_result=1 #i have initialzied the factorial result to 1 because 0!=1 ,1!=1
    for i in range(1,number+1): 
        factorial_result *=i
    
    return factorial_result
print(calculate_factorial(5))

"""
6)Function: apply_decorator
Write a Python function named apply_decorator that takes a function func as input and applies a decorator named decorator_func. The decorator should simply print "Decorator Applied" before calling the original function.
"""
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)

#eg
@apply_decorator
def greeting(name):
    print(f"Hello {name}")

greeting("dave")

"""
7)Sequences: Sort List of Tuples
Given a list of tuples where each tuple contains a name and an age, write a Python function named sort_by_age that sorts the list of tuples by age in ascending order.
"""
def sort_by_age(list):
    return sorted(list,key=lambda item:item[1])

students=[("dave",30),("felix",38),("pedro",24)]
print(sort_by_age(students))

"""
8)Sets and Dictionaries: Merge Dictionaries
Write a Python function named merge_dicts that takes two dictionaries as input and merges them into a single dictionary. If there are any common keys, their values should be summed up.
"""
def merge_dicts(dict1,dict2):
    total_dict={}
    for key in dict1:
        if key in total_dict:
            total_dict[key] +=dict1[key]
        else:
            total_dict[key]=dict1[key]
    
    for key in dict2:
        if key in total_dict:
            total_dict[key] +=dict2[key]
        else:
            total_dict[key]=dict2[key]
            
    return total_dict

dictionary1={"a":34,"b":23,"d":1}
dictionary2={"a":34,"b":2,"c":1}

print(merge_dicts(dictionary1,dictionary2))

"""
9)Object-Oriented Programming: Class Creation
Define a Python class named Car with the following attributes: make, model, year. Implement a method named display_info that prints out the car's information.
"""
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def display_info(self):
        print(f"Make:{self.make}")
        print(f"Model:{self.model}")
        print(f"Year:{self.year}")
        

my_car=Car("Mercedes-MayBach","S-class",2021)
my_car.display_info()
        