try:
    weight = float(input('Enter your weight: '))
    height = float(input('Enter your height: '))
    BMI = weight / (height/100)**2
    while True:
        if BMI <= 0:
            print('Please enter only positive numbers')
            if BMI <= 0:break
        elif BMI < 18.5:
            print('You have Underweight')
            if BMI < 18.5:break
        elif BMI <= 25:
            print('You have Normal weight')
            if BMI <= 25:break
        elif BMI <= 30:
            print('You have Overweight')
            if BMI <= 30:break
        elif BMI > 30:
            print('You have Obesity')
            if BMI > 30:break
except:
    print('Please enter only positive numbers')

