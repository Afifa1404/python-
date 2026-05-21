tup=('Python','C','Java','php')

print("Original tuple:", tup)

temp=list(tup)

temp[3]="html"

del temp[1]

tup=tuple(temp)

print("Modified tuple:", tup)

del tup