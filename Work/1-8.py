principal = 500000.0
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

print (f'{month} is required to pay ${total_paid:0.2f}')




