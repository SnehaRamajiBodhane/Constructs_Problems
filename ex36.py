#36.write a python program to print  natural number between 40 and 80 its squares and cubes ?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
print("Using for loop:")
for index in range(startrange,endingrange+1):
    print(index,index**2,index**3)

print("\n")

print("Using while loop:")
while startrange<=endingrange:
    print(startrange,startrange**2,startrange**3)
    startrange=startrange+1
print("\n")