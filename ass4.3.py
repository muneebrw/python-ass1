age = int(input('Enter your age = '))
if age < 3:
    print('Ticket is free')
elif age >= 3 and age <= 12:
    print('cost is 10$')    
else:
    print('cost is 15$')