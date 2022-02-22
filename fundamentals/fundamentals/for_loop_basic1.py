#1. Basic - Print all integers from 0 to 150.
for val in range(151):
    print(val)
    
#2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
    
for mul in range(5,1001,5):
    print(mul)

#3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for val in range(1,101):
    if(val%10 == 0):
        print("Coding Dojo")
    elif(val%5 == 0):
        print("Coding")
    else:
        print (val)
        
#4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0

for whoa in range(0, 500000):
    if(whoa % 2 != 0):
        sum += whoa

print(sum)
        
#5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for down in range(2018, 0, -4):
    print(down)


#6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum =1
highNum = 100
mult = 3
for var in range(lowNum, highNum):
    if(var%mult ==0):
        print(var)
