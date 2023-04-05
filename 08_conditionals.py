### Conditionals ###
#If a condition is true, do something
# if, elif, else


my_condition = False

if my_condition: #Works the same as if my_condition == True:
    print("This would print if my_condition is True")

my_condition = 5*2 #my_condition is 10

if my_condition == 11:
    print("This would print if my_condition is 11") #my_condition is 10

#If you want to do something if a condition is false, use else

if my_condition > 10:
    print("This would print if my_condition is greater than 10")
else:
    print("This would print if my_condition is less than or equal to 10")


#logical operators

my_condition = 15
if my_condition>10 and my_condition<20: #and means both conditions must be true
    print("This would print if my_condition is greater than 10 and less than 20") 
elif my_condition>20 and my_condition<30: #elif means else if
    print("This would print if my_condition is greater than 20 and less than 30")
else: #else means if none of the above conditions are true
    print("This would print if my_condition is not greater than 10 and less than 20")

   

print("The program continues after the if statements") #This will always print
