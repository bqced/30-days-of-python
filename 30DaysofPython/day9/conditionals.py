'''a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')'''

'''a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number') '''


'''user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')'''

'''age = int(input('Enter your age: '))
my_age = 23
young = 18 - age
if age >= 18:
    print('You are old enough drive')
if age < 18:
    print(f'you need {young} more years to learn to drive')
if age < my_age:
    print(f'i am {my_age - age} years older than you')
elif age > my_age:
    print(f'you are {age - my_age} years older than me')'''

'''num1 = int(input('enter a number: '))
num2 = int(input('Enter a number: '))
if num1 >= num2:
    print(f'{num1} is greater than {num2}')
if num1 < num2:
    print(f'{num1} is less than {num2}')
else:
    print(f'{num1} is equal to {num2}')'''

'''grade = int(input('Enter a grade: '))
if grade >= 80 and grade <= 100:
    print('your grade is A')
if grade >= 70 and grade <= 89:
    print('your grade is B')
if grade >= 60 and grade <= 69:
    print('your grade is C')
if grade >=50 and grade <= 59:
    print('your grade is D')
elif grade >= 0 and grade <= 49:
    print('your grade is F')'''

autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
summer = ['June', 'July', 'August']
spring = ['March', 'April', 'May']

'''month = input('Enter a month: ')
if month in autumn:
    print('It is autumn')
elif month in winter:
    print('It is winter')
elif month in summer:
    print('It is summer')
elif month in spring:
    print('It is spring')'''

'''fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')

if fruit in fruits:
    print(f'{fruit} is already in the list')
elif fruit not in fruits:
    fruits.append(fruit)
    print(fruits)'''

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    print(person['skills'][2])
else:
    print('The person does not have skills')
while 'skills' in person:
  if 'Python' in person['skills']:
    print('He knows Python')
    break
  else:
    print('He does not know Python')
    break

if 'Javascript' in person['skills'] and 'React' in person['skills']:
   print('He is a front end developer')
if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
   print('He is a backend developer')
if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
   print('He is a fullstack developer'),
else:
   print('unknown title')

if person['is_married'] == True:
  print(f'{person['first_name']} lives in {person['country']}. He is Married')
else:
   print('Doesnt Matter')





