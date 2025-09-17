def  goal():
    des=str(input('What is your goals for future:')).strip()
    amount=int(input('Amount of that goal thing:'))
    year=int(input('From how many year you want it:'))
    print(f'You want to save {float(amount/(year*365))} daily')

def budget():
    income=int(input('What is your Income?:'))
    bud=int(input('How much is your budget(the amount that you will spend in month?)?:'))
    if bud>income:
        print('Your budget is higher than income')
        print('please reduce your budget if you want')
        bud1=int(input('if you want to reduce please enter your budget otherwise enter 0'))
        if bud==0:
            print('previous budget added successfully')
        else:
            bud=bud1
            print('budget added successfully')
    else:
        print('budget added successfully')
