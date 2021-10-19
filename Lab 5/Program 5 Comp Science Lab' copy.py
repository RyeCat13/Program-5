import string

# first 5 characters are A-Z, first give characters of student name
#index 5 is a string value of 1 - SCE, 2 - School of Law, or 3 - College of arts and Sciences
# index 6 is either 1 - Freshman, 2 - Sophomore, 3 - Junior, 4 - Senior
# index 7 and 8 are 0-9
# index 9 is a check digit to verify the previous values (0-9)
#formular is a sum of all the values at indexes 0-8, each position is the value of the character multiplied by the index + 1
# check digit should be zero. Sum of 0-8 then modulo by 10.

if __name__ == '__main__':
    def main():
        index = 0



num_system = input('Enter Libary Card. Hit Enter to Exit ==> ')
character = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')




def invalid(not_valid):
    for i in not_valid:
        if num_system[0: 6] != character:
            print('The first 5 characters must be A-Z, the invalid character is', num_system, 'is', {}, format.num_system(int))
        if num_system not in range(0, 11):
            print('The length of the number given must be 10')
        else:
            return True

def get_school(college):
    for c in college:
        if num_system[5] == 1:
            print('The card belongs to a student in the School of Computing and Engineering SCE')
        elif num_system[5] == 2:
            print('The card belongs to a student in the School of Law')
        elif num_system[5] == 3:
            print('The card belongs to a student in the College of Arts and Sciences')
        else:
            return invalid


def get_grade(grades):
    for g in grades:
        if num_system[6] == 1:
            print('The card belongs to a Freshman')
        elif num_system[6] == 2:
            print('The card belongs to a Sophomore')
        elif num_system[6] == 3:
            print('The card belongs to a Junior')
        elif num_system[6] == 4:
            print('The card belongs to a Senior')
        else:
            return invalid

def character_value(values):
    for v in values:
        if character in range(0, 26):
            print(sum(character))
            
        
while True:
    for x in num_system:
        a = invalid(character)
        b = get_school(character)
        c = get_grade(character)
        d = character_value(character)
        print(a, b, d, c)

main()      
