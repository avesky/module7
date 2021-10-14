"""
Program: basic_list.py
Author: Andy Volesky
Last date modified: 10/13/2021

The purpose of this program:

Write a python file basic_list.py and declare two functions make_list() to return a list of user input while and get_input()
to get one input and return it.

Write the function get_input() function
prompt user for input

do not worry about validating input

Write the function make_list(num) that
asks for a given number of user input (num) in a loop by a call to get_input()
returns a string casts the input to desired type, raising exception on non-numeric input

there are a few loop options:
while loop, using symbolic constant
for loop with range()
stores them in a list

There are a a few options to add to your list.
.append(value)
use a variable to get input then .insert(index,object)
returns the list

Write your main to call your function with various numbers.
print(make_list(1))
print(make_list(2))
print(make_list(3))
"""


def get_input():
    try:
        things = int(input('Enter user input: '))
        return things
        raise ValueError("Non numeric value")
    except:
        print('Non numeric data found.')


def make_list(num):
    final_list = []
    for x in range(0, num):
        user_input = get_input()
        final_list.append(user_input)
    return final_list


if __name__ == '__main__':
    print(make_list(1))
    print(make_list(2))
    print(make_list(3))
