#1.Sum program => a,b => sum => print
#  a = int(input( "Enter a: "))
#  b = float(input ("Enter b: "))
#  sum = a + b
#  print("sum : ", sum)


#2. Take price of 3 products as input, and print the total bill amount + average price.  

# a = 99.5
# b = 23.75
# c = 16.15

# sum = a+b+c
# ave = sum/3
# print(sum)
# print(ave)


#3. build a calculator that can perform +,-,*, % and ** operations:


# a = float(input("enter a:"))
# b = float(input("enter b:"))
# op = input("Pick an operator( +, -, *, /, **, %):") #inside the bracket are options

# if op == '+' :
#      print(a+b)
# elif op == '-' :
#     print(a-b)
# elif op == '*' :
#     print(a*b)
# elif op == '/' :
#     print(a/b)
# elif op == '**' :
#     print(a**b)
# else :
#     print("INVALID OPERATOR")
# print("Thankyou!")



#4.1 print all odd numbers from 1 to 20

# for nums in range(1, 21):
#      if nums % 2 != 0 :
#         print(nums)

# for j in range ( 1, 21, 2):
#     print (j)


#4.2 print the table of 57

# i = 1
# while i <= 10 :
#     multiple= print( "57 *", i ,"=",  57 * i)
#     i = i +1
 

# for i in range(1,11):
#     print( 57, "x", i, "=", 57 * i)


    #output : 
# 57 * 1 = 57
# 57 * 2 = 114
# 57 * 3 = 171
# 57 * 4 = 228
# 57 * 5 = 285
# 57 * 6 = 342
# 57 * 7 = 399
# 57 * 8 = 456
# 57 * 9 = 513
# 57 * 10 = 570


#4.3 Print all multiples of 3 from 1 to 50 but skip 15 :

# for num in range(1,51):
#   if num == 15:
#     continue
#   print(3, "x", num, "=", 3 * num)

#4.4 Find and print the first number between 1 and 1000 is divisible by both numbers :

# a = int(input("enter first number :"))
# b = int(input("enter second number :"))

# for num in range(1,1001):
#     if num % a == 0 and num % b == 0:
#         print( "First number divisible by both: ", num)
#         break    

# a = int(input("Enter the first integer: "))
# b = int(input("Enter the second integer: "))
# for number in range(1, 1001):
#     if number % a == 0 and number % b == 0:
#      print("First number divisible by both:", number)
#      break 

# print("Thankyou")


#5.1 Print unique roll nums :

roll_numbers = [101, 105, 102, 108, 110]
print (roll_numbers)

#5.2 


