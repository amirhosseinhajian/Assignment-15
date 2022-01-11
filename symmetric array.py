input_array = input("Please enter the numbers with an space between each one:").split()
for i in range(len(input_array) // 2):
    if input_array[i] != input_array[-1 - i]:
        print("This array is not symmetric")
        break
else:
    print("This is a symmetric array")