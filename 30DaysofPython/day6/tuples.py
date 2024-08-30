# syntax
'''fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]'''

'''fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')'''

# Syntax
'''tpl = ('item1', 'item2', 'item3','item4')
print('item2' in tpl) # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' '''# TypeError: 'tuple' object does not support item assignment

# syntax
'''tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
print(tpl3)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)'''

'''fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
print(fruits) # NameError: name 'fruits' is not defined'''

'''fruits = ('cedric' , 'apple')
clear(fruits) # only works with lists'''

'''lst = ()
names = ('cedric', 'leo')
names1 = ('virginie', 'amandine')
naming = names + names1
print(naming)
print(len(naming))
names2 = ('family', 'you')
family_members = naming + names2
print(family_members)

cc, l, vi, am, *rest = family_members
print(cc, l, vi, am, *rest)'''

'''fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato')
animal_products = ('cat', 'dog', 'bird', 'fish')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
lstfoodstuff = list(food_stuff_tp)
list1 = lstfoodstuff[0:5]
list2 = lstfoodstuff[5:]
print(list1, list2)
list3 = lstfoodstuff[0:3], lstfoodstuff[-3:]
print(list3)

del food_stuff_tp
print(food_stuff_tp) #not defined
print('banana' in food_stuff_tp) # NameError: name 'food_stuff_tp' '''

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonian' in nordic_countries) # False
print('Iceland' in nordic_countries) # True