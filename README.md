import json
import os
from datetime import *
user=str(input("Enter your username:"))
# print(type(user))
if not user.isalpha():
    raise ValueError('Enter only A-Z')
else:
    print("Registration Successfully")

user_files='user.json'
def user_file():
    
    if not os.path.exists(user_files):
        return {}
    else:
        with open(user_files, 'r') as fp:
            return json.load(fp)
            

def save_file(user):
    with open(user_files,'w') as file:
        return json.dump(user,file)
    
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
def add_expenses():
    try:
        date=input("Enter Date in format (yyyy-mm-dd) or for taking automatically enter 0:").strip()
        if(date=='0'):
            date=datetime.today().strftime("%Y-%m-%d")      #to take time automatically
        else:
            date=datetime.strptime(date, '%Y-%m-%d')        #to validate time
        amount=int(input("Enter amount:"))
        cat=input("Enter category like(food, transport, household, etc):").strip()
        expense={
            'date': date,
            'amount':amount,
            'category':cat
        }
        expense.append(expense)
        save_file(expense)
    except:
        raise ValueError("Enter valid input:")
# add_expenses()  
def show_expense(expense):
    if expense==None:
        print("No Expense Record")    
    else:
        print(expense)

