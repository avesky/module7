"""
Program: topic3.py
Author: Andy Volesky
Last date modified: 10/13/2021

The purpose of this program:

What you're creating

In this assignment you will tie together the seemingly unrelated tuple and arbitrary argument list to perform
file input and output.  Your program will take a student's name and an unknown number of test scores, store them in a
tuple, save that tuple into a file, and then finally print the data from the file back to the screen.

How you're doing it

Write a function write_to_file() that accepts a tuple to be added to the end of a file
Open the file for appending (name your file 'student_info.txt')
Write the tuple on one line (include any newline characters necessary)
Close the file
Write a function get_student_info() that
Accepts an argument for a student name
Prompts the user to input as many test scores as they wish
Stores the information (name and scores) in a tuple
Calls the function write_to_file() sending the tuple to be written to the end of the file
Write a function read_from_file() that
Reads a file line by line
Prints each line to the console
In main
Call the get_student_info() for at least 4 different students.
Call read_from_file()
"""
import os as os


def write_to_file(the_tuple):
    f = open('student_info.txt', 'a')
    f.writelines(f'{the_tuple}\n')
    f.close()


def get_student_info(name):
    test_list = []
    user_number = int(input('Enter a number between 1 and 100 (999 to stop): '))
    while user_number != 999:
        while 1 > user_number or user_number > 100:
            user_number = int(input('Enter a good number please: '))
            if user_number == 999:
                break
        if user_number == 999:
            break
        test_list.append(user_number)
        user_number = int(input('Enter a number between 1 and 100 (999 to stop): '))
    the_tuple = (name, str(test_list))
    write_to_file(the_tuple)

def read_from_file():
    f = open('student_info.txt', "r")
    lines = f.readlines()
    print(lines)
    f.close()

if __name__ == '__main__':
    # 1st part
    # the_tuple = ('1', '2', '3', '4', '5')
    # 2nd part
    # write_to_file(the_tuple)
    # 3rd part
    # get_student_info('Dave')
    # 4th part
    # read_from_file()
    # 5th part
    get_student_info('Aang')
    get_student_info('Uncle Iroh')
    get_student_info('Katara')
    get_student_info('Appa')
    get_student_info('Momo')
    read_from_file()