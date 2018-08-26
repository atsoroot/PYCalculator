#CREDITS
credits = "<> with <3 by atsoroot."
#Define add function
#X is first number and Y is secound number
def add(x, y):
   return x + y
#Define add subtract
def subtract(x, y):
   return x - y
#Define multiply function
def multiply(x, y):
   return x * y
#Define divide function
def divide(x, y):
   return x / y

print("Select operation.")
print()
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print()

choice = input("Enter choice (1|2|3|4):")
print()
num1 = int(input("Enter first number: "))
print()
num2 = int(input("Enter second number: "))
print()

if choice == '1':
   print("The added number is: ", add(num1,num2))
   print()
   print(credits)

elif choice == '2':
   print("The subtracted number is: ", subtract(num1,num2))
   print()
   print(credits)

elif choice == '3':
   print("The multiplied number is: ", multiply(num1,num2))
   print()
   print(credits)

elif choice == '4':
   print("The devided number is: " , divide(num1,num2))
   print()
   print(credits)
else:
   print("Invalid input")

print()
input("Press enter to exit ;)")
