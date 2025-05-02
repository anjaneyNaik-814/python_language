input1= input("Enter a number or string: ")
input2= input("Enter a number or string: ")

if input1.isdigit() and input2.isdigit():
    print(f"Sum of the two numbers is {int(input1)+int(input2)}")

else:
    print(f"Concatenation of the two strings is {input1+input2}")