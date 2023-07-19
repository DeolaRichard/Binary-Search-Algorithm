def binary_search(list, element):
    start = 0
    middle = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print("step", steps, ":", str(list[start:end + 1]))

        steps = steps + 1
        middle = (start + end) // 2

        if element == list(middle):
           return middle
        if element < list(middle):
            return middle - 1
        else:
            return middle + 1

    return -1
