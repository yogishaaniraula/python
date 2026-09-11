#Arithmetic operators
# print(5-3)
# print(5%3) # modulo -> remainder
# print(5**3) #power


#Assignment operators
# x = 2
# x += 7 # ( x = x+7)
# print (x) # 9

#Operator precedence ( BODMAS )
# () > *,/ > +, - 

# if * and / on same line : move from left to right

#comparision operators
# >,<, >=, <=, ==, != 
# print(2>=8) #false
# print(8<=10) #true
# print(2==2) #true
# print (5!=5) #false

#logical operators
# or, and, not 
# st1 = 3>5 #false
# st2 = 3>2 # true

# print(st1 or st2) # ans = true because for OR, if one is true ans is true

# st1 = 3>1
# st2 = 3<8

# print (st1 and st2) # ans = true because for AND, if both are true ans is true 


# print(not (3>2)) #false 


#Conditional statements

# age = int(input("enter age:"))

# if age >= 18:
#     print("you are an adult") #indentation : leaving proper space and gaping
#     print("you can drive and vote")
# elif  age < 18:# else if  
#     print("you can't drive or vote")

# print("end of code") # this code will run irrespective to the age because it is outside the if code (separated by the gaps)


marks = int(input("Enter your marks"))

if marks >=80:
    print("A")
elif marks <80 and marks >= 60:
    print("B")
else :  # if it is the last statement, then you can write else, and you dont have to mention conditions like you did on elif.
    print("C")
    
print("Congratulation!")






