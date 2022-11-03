def input_weight():
    try:
        weight = float(input('Enter your weight: '))
        check_positive_weight(weight=weight)
        return weight
    except:
        print('Please enter only positive numbers weight!')
        weight = input_weight()
        return weight


def input_height():
    try:
        height = float(input('Enter your height: '))
        check_positive_height(height=height)
        return height
    except:
        print('Please enter only positive numbers height!')
        height = input_height()
        return height

def calculation_BMI(weight, height):
    BMI = weight / (height/100) ** 2
    return BMI

def check_positive_weight(weight):
    if weight <= 0:
        print('Please enter only positive numbers weight!')
        input_weight()

def check_positive_height(height):
    if height <= 0:
        print('Please enter only positive numbers height!')
        input_height()

def check_BMI(BMI):
    while True:
        if BMI < 18.5:
            print('You have Underweight')
            break
        elif BMI <= 25:
            print('You have Normal weight')
            break
        elif BMI <= 30:
            print('You have Overweight')
            break
        elif BMI > 30:
            print('You have Obesity')
            break

def main_code():
    weight = input_weight()
    height = input_height()
    BMI = calculation_BMI(weight=weight, height=height)
    check_BMI(BMI=BMI)








