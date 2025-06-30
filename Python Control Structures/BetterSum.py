# Enter your code here
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
sum = num1
sum2 = num1
for i in range(num1, num2):
    sum += 1
    sum2 += sum
    print(sum2)