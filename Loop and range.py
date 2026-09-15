#range : sequence of 0 to n-1

# nums = range(5) 
# print (nums) 

# to print 1 to 5, we write range(5) or range(0,5)

#range(start= 0 by default, stop= always pass by coder, step= 1 by default)


#loops

# counter = 1
# while counter <=5:
#     print("hi there", counter)
#     counter += 1
# print("end of code") 

#output : hi there 1
# hi there 2
# hi there 3
# hi there 4
# hi there 5
# end of code


# i = 1
# while i <=5:
#      print(i * "i") # whenever an integer value is mulitpled by a string, the output the multiple of the string.  
#      i += 1
# print("end of code") 

#output : 
# i      (1 * i = i)
# ii     (2 * i = i i) and so on..
# iii
# iiii
# iiiii


# i = 5 
# while i > 0 :
#     print ( i * "hello ")
#     i -= 1  # i = i -1 = 5 -1 = 4 

#output : 
# hello hello hello hello hello  ( 5 * hello = hellohellohellohellohello )
# hello hello hello hello  ( 4 * hello = hellohellohellohello)
# hello hello hello 
# hello hello 
# hello 

#For loops

# for numbers in range(0,5): # 0 to 4
#     print(numbers) 

#output : 
# 0
# 1
# 2
# 3
# 4

# for nums in range(0,12,2): # the last value is not included
#    print(nums)
#output : 
# 0
# 2
# 4
# 6
# 8
# 10

# for numb in range(1,11) : #checking values for these numbers
#     if numb % 2 == 0:
#         print(numb)

# for i in range(2, 11, 2):
#      print (i)

#Break and Continue :
#break : stops the code 
#continue : skips the code

#print all the multiples of 3 but 21 then stop, range(1, 50)

# for numbs in range(3,51, 3) :
#     print (numbs)
#     if numbs == 21:
#       print("End of code")
#       break # stops the code


# for num in range (1, 51):
#    if num == 21:
#       continue # code below this line won't run, because it will move up towards the initial line

#    if num % 3 ==0 : # this is the main logic of the code, for 21, this logic won't be applied. It has been skipped
#       print(num)
 
# print("out of loop")

    














