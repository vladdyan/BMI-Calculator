try:
    weight = float(input('Enter your weight: '))
    height = float(input('Enter your height: '))
    BMI = weight / (height/100)**2
    while True:
        if BMI <= 0:
            print('Please enter only positive numbers')
            break
        elif BMI < 18.5:
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
except:
    print('Please enter only positive numbers')

