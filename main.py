import csv

DAILY_LIMIT = 5000
BASE_CURRENCY = "INR"
value_currency ={"USD":95.05, "INR":1.0}
WARNING_LIMIT =4000

expenses = [
    {"emp_id": "E001", "emp_name": "Karan Yadure","category":"Travel", "amount":150.00, "currency": "USD"},
    {"emp_id": "E002", "emp_name": "Jay Sankar","category":"Food", "amount":4500.00, "currency": "INR"},
    {"emp_id": "E003", "emp_name": "Tomy Varsati","category":"Software", "amount":650.00, "currency": "USD"},
]

for expense in expenses:
    rate = value_currency[expense["currency"]]
    expense["amount_inr"] = expense["amount"]*rate
    if expense["amount_inr"] > DAILY_LIMIT:
        expense["flag"] ="^ OVER LIMIT "
        
    elif expense["amount_inr"] > WARNING_LIMIT :
        expense["flag"] ="~NEAR LIMIT "
    else :
        expense["flag"] ="OK"
    
for expense in expenses:
        print(f"STATUS : {expense['flag']} |" 
          f"ID: {expense['emp_id']}  |  " f"Name: {expense['emp_name']}  |  "
          f"Category: {expense['category']}  |  "
          f"Amount:  rs {expense["amount_inr"]:.2f} IN {expense['currency']}" )





