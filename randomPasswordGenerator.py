import random

def random_password_generator():    
    length = int(input("Enter length of password to be generated: "))
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numericals = "0123456789"
    special_characters = "[]{}()*;/,._-=&%$#@!^"
    compilation = lower_case + upper_case + numericals + special_characters
    pass_gen = "".join(random.sample(compilation, length))
    return pass_gen

random_password_generator()
