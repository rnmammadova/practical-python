"""bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)"""


"""height=100
drop=1
while drop <= 10:
    drop=drop+1
    height=height*3/5
    print(drop, height)"""



"""principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month=0

while principal > 0:    
    month=month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if month <= 12:
        principal=principal-1000
        total_paid=total_paid+1000

print('Total paid', total_paid)
print('Total month', month)

print (f'{month} is required to pay ${total_paid:0.2f}')"""

print("hello")



