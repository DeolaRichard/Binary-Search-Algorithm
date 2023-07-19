def binary_search(dist, element):
    middle = 0
    start = 0
    end = len(dist)
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
            end = middle + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target = 2

binary_search(my_list, target)
