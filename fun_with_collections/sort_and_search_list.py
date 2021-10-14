"""
Program: sort_and_search_list.py
Author: Andy Volesky
Last date modified: 10/13/2021

The purpose of this program:

Write sort_list() to sort the list

What is the return statement?
    Write a comment explaining why you included return OR
    Write a comment explaining why your code has no return statement.

Write search_list()
    What is the return statement?
    Write a comment explaining why you included return OR
    Write a comment explaining why your code has no return statement.

Write main
call sort_list()
call search_list()
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

def sort_list():
    new_list = make_list(5)
    new_list.sort()
    return new_list
# .sort() sorts the list in place and returns none, so I made a new list and sorted that list then returned the new list


def search_list(value):
    new_list = make_list(5)
    searched = new_list.index(value)
    print(new_list)
    return searched
# I returned searched to get the index of the value that we are searching for

if __name__ == '__main__':
    print(sort_list())
    print(search_list(99))