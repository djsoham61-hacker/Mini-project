import json
import os
from datetime import *
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
show_expense(expense=add_expenses)

