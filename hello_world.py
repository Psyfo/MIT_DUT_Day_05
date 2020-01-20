# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:02:08 2020

@author: Admin
"""

def get_name():
    name = input("What is your name? ")

    print("My name is " + name + " (Concatenation)")
    print("My name is",name,"(Comma notation)")
    print("My name is {} (Positional arguments)".format(name))
    print(f"My name is {name} (F strings)")
    
def dict_prac_01():
    grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
    name = input("Whose grade do you want? ")
    if name in grades.keys():
        print(f'{name} earned a grade of: {grades[name]}')
    else:
        print('That name cannot be found')


dict_prac_01()
    
