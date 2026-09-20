# # tuple are immutable. If you want to create a new tuple, you have to create a new tuple


# marks = (46,89, 95, 86, 80, 75, 86, 86)
# print(marks[2]) # otpt: 95

# print(marks.index(80)) # otpt: 4 
# print(marks.count(75)) #otpt: 1
# print(marks.count(86)) #otpt: 3


# Set : unique items collection

marks = {46,89, 95, 86, 80, 75, 86, 86}
#print(len(marks)) # output : 6. It doesn't count repeated numbers, only the unique ones.

# for score in marks:
#     print(score) 


#dictionary is a collection of key value pairs {key =>value}

marks = { "Math :": 99, "Physics :": 89, "Chemistry :": 83} 

print(marks, type (marks))
print(marks["Physics :"])

for key in marks :
    print(key,marks [key])

