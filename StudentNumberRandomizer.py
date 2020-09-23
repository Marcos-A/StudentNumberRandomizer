#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Assign a random number to each student contained in a list.
The student list is randomly sorted as well.
The result is stored in a log file and printed in the
screen (press Enter to advance through the list).
"""

import random

students_list = ['Álex','Amy', 'Alba', 'Andrea', 'Arantza', 'Carol',
                 'Chaimae', 'David', 'Enis', 'Eva', 'Fran', 'Iván', 'Jair',
                 'Kenia', 'Ling', 'Manel', 'Miriam', 'Nerea', 'Nora', 'Raquel',
                 'Saray', 'Yaiza', 'Yara', 'Youseff']

student_number_assignment = {}

"""
Fill a dict passed as a param to store students randomly selected from a list
as keys, and a number randomly selected beteween 1 and 10 as values.
"""
def randomize_students_and_numbers(student_number_assignment):
    while students_list:
        random_student = random.choice(students_list)
        students_list.remove(random_student)

        student_number_assignment[random_student] = random.choice(range(1, 11))
    
    return student_number_assignment


"""
Generate a log with the result of randomize_students_and_numbers(student_number_assignment)
"""
def generate_log(student_number_assignment):
    raffle_result = open('result.log', "w+")
    for student in student_number_assignment:
        raffle_result.write('Estudiant: ' + student +
                            '\nPregunta: ' + str(student_number_assignment[student]) +
                            '\n\n')

    raffle_result.close()


"""
Print the result of randomize_students_and_numbers(student_number_assignment).
Press Enter to advance through the whole list.
"""
def screen_printer(student_number_assignment):
    print('\n')
    for student in student_number_assignment:
        print('Estudiant: ' + student +
              '\nPregunta: ' + str(student_number_assignment[student]))
        input()

    print('__________END__________\n')


if __name__ == "__main__":
    student_number_assignment = randomize_students_and_numbers(student_number_assignment)
    generate_log(student_number_assignment)
    screen_printer(student_number_assignment)
