import csv

DAILY_LIMIT = 5000
BASE_CURRENCY = "INR"
VALUE_CURRENCY ={"USD":95.05, "INR":1.0}

expenses = [
    {"emp_id": "E001", "emp_name": "Karan Yadure","category":"Travel", "amount":150.00, "currency": "USD"},
    {"emp_id": "E002", "emp_name": "Jay Sankar","category":"Food", "amount":4500.00, "currency": "INR"},
    {"emp_id": "E003", "emp_name": "Tomy Varsati","category":"Software", "amount":650.00, "currency": "USD"},
]

for expense in expenses:
    print(f"ID: {expense['emp_id']}  |  "
          f"Name: {expense['emp_name']}  |  "
          f"Category: {expense['category']}  |  "
          f"Amount: {expense['amount']} {expense['currency']}" )





