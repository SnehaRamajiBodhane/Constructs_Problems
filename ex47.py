#47.write a python program to print even number between num1 and num2  and its sqaures and cubes where num1>1 num2>2 in reverse order?
num1=num2=0
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
print("Using for loop:")

for i in range(num1,num2+1):
    if (num2%2!=0):
        print(num2,num2**2,num2**3)
    num2=num2-1

num1=num2=0
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
print("Using while loop:")
while num1<=num2:
    if num2%2!=0:
        print(num2,num2**2,num2**3)
    num2=num2-1