import json
import os
from datetime import *
from reg import login, registration
user_files = login()

def user_file():
    
    if not os.path.exists(user_files):
        return {"Username": user_files, "Expenses": []}
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
        data = user_file()
        if "Expenses" not in data:
            data["Expenses"] = []
            data['Expenses'].append(expense)
        else:
            data['Expenses'].append(expense)
        
        save_file(data)
    except ValueError as v:
        print("Enter valid input:",v)
add_expenses()  
def show_expense():
    data = user_file()
    expense1 = data.get("Expenses",[])
    if expense1==None:
        print("No Expense Record")    
    else:
        
        for e in expense1:
            print({e['date']},'| |',{e['amount']},'| |',{e['category']})
            print('\n')
            
show_expense()
# show_expense()
