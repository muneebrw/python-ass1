dict = {'First_name' : 'Muneeb',
        'Last_name' : 'Raza',
        'Age' : '20',
        'City' : 'Karachi'}
for x,y in dict.items():
    print(x + " : " + y)

dict['Edu'] = 'Intermediate'

print('A D D E D')
for x,y in dict.items():
    print(x + " : " + y)

dict['Edu'] = 'BCS'
print('U P D A T E D')
for x,y in dict.items():
    print(x + " : " + y)
    
del dict['Edu']
print('D E L E T E D')
for x,y in dict.items():
    print(x + " : " + y)
    