# Enter your code here
def square(x):
     squ_are = x**2
     return (squ_are)


print("5 squared is ")
x = (square(5))
print(x)

print("6 squared is")
x = (square(6))
print(x)

user = int(input("What number do you want to square? "))
print(square(user))