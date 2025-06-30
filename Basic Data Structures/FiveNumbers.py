nums = []


for i in range(5):
    num = int(input("Number: "))
    nums.append(num)
    print(nums)
total = sum(nums)
print("Sum: " + str(total))