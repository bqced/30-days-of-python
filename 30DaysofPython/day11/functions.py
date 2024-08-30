from math import prod
from statistics import median, mode, variance, stdev, mean
'''def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()'''

'''def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))'''

'''def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))'''

'''def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)#returns None because we havent used return
print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total) #returns None because we havent used return
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter'''

'''def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))'''

'''def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))'''

'''def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27'''

'''def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(5, 10))

def area_of_circle(r):
    pi = 3.14
    return pi * (r ** 2)
print(area_of_circle(3))

def add_all_nums(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        elif isinstance(arg, list):
            total += sum(arg)
        else:
            return f"Error: {arg} is not a number or a list"
    return total

print(add_all_nums([2, 3, 5, 7, 8, 9])) 

def convert_celsius_to_fahrenheit(c):
    return c * (9/5) + 32
print(convert_celsius_to_fahrenheit(32))'''

'''def check_season(month):
    autumn = ['September', 'October', 'November']
    winter = ['December', 'January', 'February']
    summer = ['May', 'June', 'July']
    spring = ['March', 'April', 'May']
    if month in autumn:
        return 'Autumn'
    elif month in summer:
        return 'Summer'
    elif month in winter:
        return 'Winter'
    elif month in spring:
        return 'Spring'
print(check_season('September'))

def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
      print("The line is vertical, slope is undefined.")
    else:
        slope = (y2 - y1) / (x2 - x1)
    return slope

print(calculate_slope(1, 2, 4, 6))'''


'''def print_list(lst):
    for item in lst:
        print(item)

test_list = [1, 2, 4, 6, 8, 8]
print(print_list(test_list))'''

'''def reverse_array(lst):
    return lst[::-1]
    
lst = [1, 2, 4, 6]
print(reverse_array(lst))'''

'''def reverse_list(arr):
   left = 0
   right = len(arr) -1
   while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
   return arr

arr = [1, 2, 4, 5 ,7]
arr = ['A', 'B', 'C', 'D']
print(reverse_list(arr))
print(reverse_list(arr))'''

'''def capitalize_items(lst):
    capitalized_list = []
    for item in lst:
        if isinstance(item, str):
            capitalized_list.append(item.capitalize())
        else:
            capitalized_list.append(item)  # Non-string items are left unchanged
    return capitalized_list

lst = ['apple', 'banana', 'cherry']
print(capitalize_items(lst))'''

'''def add_item(lst, item):
    lst.append(item)
    return lst
lst = [1, 3 ,4 ,5]
print(add_item(lst, 78))
lst = ['banana', 'cherry', 'apple']
print(add_item(lst, 'blueberry'))'''

'''def remove_item(lst, item):
    lst.remove(item)
    return lst

lst = [1, 3 ,4 ,5]
print(remove_item(lst, 3))
lst = ['banana', 'cherry', 'apple']
print(remove_item(lst, 'banana'))'''

'''def sum_numbers(n):
    return sum(range(n + 1))

print(sum_numbers(7))

def sums(n):
    sum_odd = 0
    sum_even = 0
    for item in range(n + 1):
        if item % 2!= 0:
            sum_odd += item
        elif item % 2 == 0:
            sum_even += item
    print(f"Even number is {sum_even}")
    print(f"Odd number is {sum_odd}")

print(sums(5))'''

'''def factorial(n):
    return prod(range(1, n + 1))

print(factorial(4))

def is_empty(*args):
    if not args:
        return 'It is Empty'
    item = args[0]
    if isinstance(item, (str, int, float, list, dict, set, tuple)):
        return 'It is not empty'
    else:
        return 'Unknown type'

# Test cases
print(is_empty())              
print(is_empty(""))            
print(is_empty("Hello"))       
print(is_empty([]))   '''

'''def calculate_all(lst):
    if not lst:
        return "Empty list"
    return {
        "mean": mean(lst),
        "median": median(lst),
        "mode": mode(lst),
        "range": max(lst) - min(lst),
        "variance": variance(lst),
        "std_dev": stdev(lst)
    }
   
lst = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

print(calculate_all(lst))'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return 'It is a prime number'

print(is_prime(43))

