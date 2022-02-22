#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ]
#1.1. x[1][0] = 15
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#1.2. students[0]['last_name'] = 'Bryant'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
#1.3. sports_directory['soccer'][0] = 'Andres'
z = [ {'x': 10, 'y': 20} ]
#1.4. z[0]['y'] = 30



#2 Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""
def iterateDictionary(students):
    for ind in range (len(students)):
          for val in range (len(students[ind])):
              print((list(students[ind].keys())[val]) + " - " + (list(students[ind].values())[val]))
"""



#3 Get Values From a List of Dictionaries
"""
def iterateDictionary2(key_name, some_list):
    for ind in range(len(some_list)):
        print(some_list[ind][key_name])
"""



#4 Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon

"""
def printInfo(some_dict):
    for ind in some_dict:
        print((len(some_dict[ind])), (ind.upper()))
        for items in some_dict[ind]:
            print(items)
"""
