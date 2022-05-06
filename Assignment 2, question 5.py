a=float(input('Enter first side '))
b=float(input('Enter second side '))
c=float(input('Enter third side '))

Result = ((a+b>c) & (a+c>b) & (b+c>a)) ==1

print(str(Result).replace('True','Yes').replace('False', 'No'))
