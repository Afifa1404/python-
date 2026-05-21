student={"Name":"Afifa","Age":18,"Regno":162,"Branch":"CSE"}
print("Keys are:")
for x in student:
    print(x)
print("Values are:")
for x in student:
    print(student[x])
print("Keys and values are:")
for x,y in student.items():
    print(x,y)