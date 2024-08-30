#Day 2: 30 Days of python programming'
first_name = 'cedric'
last_name = 'junior'
full_name = 'cedric junior'
country = 'united kingdom'
city = 'manchester'
age = 23
year = 2024
is_married = False
is_true = True
is_light_on = False
info = first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on

type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)
name_length = len(first_name)
print(name_length)
lastname_length = len(last_name)
print(lastname_length)

if lastname_length > name_length:
 print('last name is longer')
if name_length > lastname_length:
 print('name is longer')
else:
 print('both are the same lenght')

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one/num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
area_of_circle = 3.14*30**2
circum_of_circle = 2 * 3.14 * 30
radius = input('Enter radius' )
area_circle = 3.14 * int(radius)**2
print(area_circle)

name = input(str('Enter a name  '))
last_name = input(str('Enter a last name  '))
country = input(str('Enter country  '))
age = input('Enter age  ')