w = float(input('Enter your weight: '))
h = float(input('Enter your height: '))
bmi = w / (h/100)**2
while True:
    if bmi < 18.5:
        print('You have Underweight')
        if bmi < 18.5:break
    elif bmi <= 25:
        print('You have Normal weight')
        if bmi <= 25:break
    elif bmi <= 30:
        print('You have Overweight')
        if bmi <= 30:break
    elif bmi > 30:
        print('You have Obesity')
        if bmi > 30:break
