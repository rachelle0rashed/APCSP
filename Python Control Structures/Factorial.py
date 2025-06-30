factorial = 1
N = int(input( "What is the number: "))

for i in range(1, N+1):
    factorial = factorial * i
    print(factorial)