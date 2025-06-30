last_name_list = []
for i in range(0,5):
    full_name = input("Name: ")
    name_list = full_name.split()
    last_name = name_list[-1]
    last_name_list.append(last_name)
    last_name_list.sort()
print(last_name_list)