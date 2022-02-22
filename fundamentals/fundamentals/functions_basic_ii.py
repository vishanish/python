#1 Countdown
def countdown(num_1):
    my_list = []
    for x in range(num_1,-1,-1):
        my_list.append(x)
    return my_list

print(countdown(5))

#2 Print and Return
def printreturn(num):
    for x in range(len(num)):
        print(num[0])
        return(num[1])

printreturn([2,3])

#3 First and Length
def first_and_length(my_list):
    return my_list[0] + len(my_list)

first_and_length([1,2,3,4,5])

#4 Values Greater than Second
def values_greater_than_second(my_list1):
    my_list2 = []  
    if(len(my_list1)<2):
        return False
    else:
        for x in (my_list1):
            if(x > my_list1[1]):
                my_list2.append(x)
    return my_list2

values_greater_than_second([7,8,9,10,11])

#5 This Length, That Value
def length_and_value(size, value):
    my_list = []
    for x in range (size):
        my_list.append(value)
    return my_list

length_and_value(5,10)
