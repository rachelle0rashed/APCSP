text = input("Enter some text: ")
indices = []
count = 0
my_list = text.split()
for owl, word in enumerate(my_list):
        if "owl" in word:
            indices.append(owl)
            count += 1
print("There were " + str(count) + " words that contained 'owl'." )
print("They occurred at indices " + str(indices))