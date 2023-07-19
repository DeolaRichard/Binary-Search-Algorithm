def binary_search(dist, element):
    middle = 0
    start = 0
    end = len(dist) - 1  # Subtract One to accommodate Zero Indexing
    steps = 0

    while start <= end:
        print("Step", steps, ":", str(dist[start:end + 1]))

        steps = steps + 1
        middle = (start + end) // 2

        if element == dist[middle]:
            return middle
        if element < dist[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


# collecting data from the user

# Creating an empty list
my_list = []

# Ask the User for the number of inputs they want to add
num_inputs = int(input("How many inputs are you entering?"))

# Collect the inputs and add them to the list
for i in range(num_inputs):
    user_input = int(input("Enter input {}: ".format(i + 1)))
    my_list.append(user_input)

print("Your inputted data is: ", my_list)

# Accept a single integer value for the target value

# Ask the user for the value of the target
target = int(input("What is your target value?"))

result = binary_search(my_list, target)

if result != -1:
    print("Target Value found at index: ", result + 1)  # Add One to accommodate zero indexing
else:
    print("Target Value not found in list.")
