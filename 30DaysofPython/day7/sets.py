# syntax
'''st = {'item1', 'item2', 'item3', 'item4'}
len(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')'''

# syntax
'''st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)'''

# syntax
''' = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2') #remove specified item
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()  #removes random item
print(removed_item)
print(fruits)'''

'''fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
print(st) # NameError: name 'st' is not defined'''

'''fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
fruits1 = tuple(fruits) #('mango', 'lemon', 'banana', 'orange) '''

'''fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
stp1 = vegetables.union(fruits)
print(stp1)
print(fruits.union(vegetables)) '''

# syntax
'''st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
print(st1)'''

# syntax
'''st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
x2 = st1.intersection(st2) # {'item3', 'item2'}
print(x2)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
x1 = whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
print(x1)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
x = python.intersection(dragon)     # {'o', 'n'}
print(x)'''

# syntax
'''st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
x = st2.issubset(st1) # True
st1.issuperset(st2) # True
print(x)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
x1 = whole_numbers.issubset(even_numbers) # False, because it is a super set
x2 = whole_numbers.issuperset(even_numbers) # True
print(x1, x2)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
x3 = python.issubset(dragon)     # False
print(x3) '''

# syntax
'''st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
x = st2.difference(st1) # set()
x1 = st1.difference(st2) # {'item1', 'item4'} => st1\st2
print(x,'#', x1)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
x2 = whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}
print(x2) '''

'''python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
x3 = python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
x4 = dragon.difference(python)     # {'d', 'r', 'a', 'g'}
print(x3, '#', x4) '''

'''whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}'''

# syntax
''' st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item '''

#print(A.union(B).difference(A)) #does union of sets then does difference of A from union of A and B

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies)) # 7
it_companies.update(['Twitter'])
print(it_companies)

companies = ['Tesla', 'Nvidia', 'ASML']
it_companies.update(companies)
print(it_companies)
print(it_companies.remove('Facebook'))

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B),B.union(A))
print(A.symmetric_difference(B))
print(A.clear(), B.clear())

x = set(age)
x1 = age
print(len(set(age)), len((age))  )
print(x, x1) # set removed duplicates and sorted in ascending order
#list stay the same

#sets are unordered, mutable(but only immunate object can be stored in(eg: string ,int, float)), stored in curly braces{}
#tuple immunatable, can store any objects, stored in parentheses()
#list mutable, can store any objects, stored in square brackets[]
#Dictionaries are used to store data values in key:value pairs.


