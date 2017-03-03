# Practicing python with MIT Courses
pi = 3.1419
radius = 2.2
area = pi * (radius ** 2)
radius += 1
# print('Area is ', area)
# print('Radius is ', radius)


def check_number(userInput):
    if userInput % 2 == 0:
        print('It is an even number')
    else:
        print('The number is Odd')


def divison_checker(userInput):
    if userInput % 2 == 0:
        if userInput % 3 == 0:
            print('Your Number can be divided by 2 and 3')
        else:
            print('Your Number can only be divided by 2')
    elif userInput % 3 == 0:
        print('Your Number is only divisible by 3 and not by 2')


def max_number_three(number1, number2, number3):
    if number1 > number2:
        if number1 > number3:
            print(number1, ' is Biggest number')
        else:
            print(number3, ' is Biggest number')
    elif number2 > number3:
        print(number2, ' is Biggest number')
    else:
        print(number3, 'is Biggest number')


def least_number_three(number1, number2, number3):
    if number1 < number2:
        if number1 < number3:
            print(number1, ' is least number')
        else:
            print(number3, ' is least number')
    else:
        print(number2, ' is least number')


def middle_number_three(number1, number2, number3):
    if number1 <= number2 <= number3 or number3 <= number2 <= number1:
        print(number2, ' is the middle number')
    elif number2 <= number1 <= number3 or number3 <= number1 <= number2:
        print(number1, ' is the middle number')
    else:
        print(number3, ' is the middle number')


def average_number_three(number1, number2, number3):
    average = (number1 + number2 + number3) / 2
    print(average, ' is average of three numbers')


def ultimate_number_checker():
    input1 = float(input('Please enter the first number: '))
    input2 = float(input('Please enter the second number: '))
    input3 = float(input('Please enter the third number: '))
    least_number_three(input1, input2, input3)
    max_number_three(input1, input2, input3)
    middle_number_three(input1, input2, input3)
    average_number_three(input1, input2, input3)


def user_data():
    username = input('Please enter your name: ')
    age = int(input("What's your age " + username + ': '))
    if age > 100:
        print("WOW you are over 100 Old Guy.")
    else:
        print('You have only ', 100 - age, " years left before turning to 100")


user_data()
# Now I am chaning this comment from github as another user
