"""
Program: topic2.py
Author: Andy Volesky
Last date modified: 10/13/2021

The purpose of this program:

Complete the average_scores() functions using arbitrary argument lists and keyword arguments and returning a string
in the following format (for example, you will have your own):

"""

def average_scores(*args, **kwargs):
    for key, value in kwargs.items():
        if key == 'first_name':
            f_name = value
        if key == 'last_name':
            l_name = value
        if key == 'major':
            maj = value
    # Use *args for average calculation
    total = 0
    count = 0
    for arg in args:
        total = total + arg
        count = count + 1
    return f'Name = {f_name} {l_name}, GPA = {total/count}, Major = {maj}'

if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))
    print(average_scores(3, 3.25, 1, 4, first_name='Dave', last_name='Coulier', major='Cutting It Out'))
    print(average_scores(4, 4, 4, 4, first_name='Mary', last_name='Straight_As', major='Basket Weaving'))