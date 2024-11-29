
#if -elif-else statements 

marks = int(input("Enter your marks : "))

if(marks<100 and marks>90):
    print("A Grade")

elif(marks<89 and marks>70):
    print("B Grade")

elif(marks<69 and marks>45):
    print("C Grade")

else:
    print("D Grade")