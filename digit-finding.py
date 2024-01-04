#1st way
num = int(input("Number: "))
count = 0

while num != 0:
    num //= 10
    count += 1
print("Number of digits: " + str(count))

#2nd way
num1 = input("Son: ")
num2 = list(num1)
print(num2)
print("Uzunligi: ", len(num1))





