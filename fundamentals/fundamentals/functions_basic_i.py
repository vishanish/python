#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Output: Predict: 5; Actual: 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Output: Predict: 12; Actual: NameError: name 'number_of_days_in_a_week_silicon_or_triangle_sides' is not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Output: Predict: 5; Actual: 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Output: Predict: 5; Actual: 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Output: Predict: 5 None; Actual: 5 None

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# Output: Predict:  3 5 None; Actual: 3 5 TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Output: Predict: 25; Actual: 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Output: Predict: 100 10 7; Actual: 100 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# Output: Predict: 7; Actual: 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Output: Predict: 14; Actual: 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Output: Predict: 21; Actual: 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Output: Predict: 8; Actual: 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# Output: Predict: 500 500 300 500; Actual: 500 500 300 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# Output: Predict: 500 500 300 None 500; Actual: 500 500 300 300 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# Output: Predict: 500 500 300 300 300; Actual: 500 500 300 300 

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Output: Predict: 1 3 2; Actual: 1 3 2 

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# Output: Predict: 1 3 5 10; Actual: 1 3 5 10
