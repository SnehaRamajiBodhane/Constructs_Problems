#42.write a python program to print Natural Number between num1 and num2 and its squares and cubes where num1>1 num2>2?
num1=num2=0
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
print("Using for loop:")

for i in range(num1,num2+1):
    print(i,i**2,i**3)


print("Using while loop:")


while num1<=num2:
    print(num1,num1**2,num1**3)
    num1=num1+1