import json
import os
from datetime import *

user_files='user.json'
def user_file():
    
    if not os.path.exists(user_files):
        return[]
    else:
        with open(user_files, 'r') as fp:
            return json.load(fp)   #convert in to Json Format
            

def save_file(user):
    with open(user_files,'w') as file:
        return json.dump(user,file)   #Write in JSON fromat directly
    

def add_expenses():
    try:
        date=input("Enter Date in format (yyyy-mm-dd) or for taking automatically enter 0:").strip()
        if(date=='0'):
            date=datetime.today().strftime("%Y-%m-%d")      #to take time automatically
        else:
            date=datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')        #to validate time
        amount=int(input("Enter amount:"))
        cat=input("Enter Reason like(food, transport, household, etc):").strip()
        expense={
            'date': date,
            'amount':amount,
            'category':cat
        }
        user = user_file()
        user.append(expense)
        
        save_file(user)
    except ValueError as v:
        print("Enter valid input:",v)
add_expenses()  
def show_expense():
    expense1 = user_file()
    if expense1==None:
        print("No Expense Record")    
    else:
        
        for e in expense1:
            print(e['date'],e['amount'],e['category'])
            
show_expense()
# show_expense()
