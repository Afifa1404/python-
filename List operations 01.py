numbers=[10,20,30,40]
print("Original List:",numbers)
numbers.append(50)
print("After Append:",numbers)
numbers.insert(2,25)
print("After insert:",numbers)
numbers.remove(30)
print("After remove:",numbers)
print("Length of list:",len(numbers))
print("List elements:")
for item in numbers:
    print(item)