# i   arr                         swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]

        # OR FINISH LIKE THIS

# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 5, 4, 7, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (4,5)


# i   arr                         swap (indices)
# 0   v   swap (1,6)
# 1   [7, 6, 3, 2, 4, 5, 1]   swap (0,6)
# 2   [1, 6, 3, 5, 4, 2, 7]   swap (3,5)
# 3   [1, 6, 3, 5, 4, 2, 7]   swap (1,5)
# 4   [1, 2, 3, 5, 4, 6, 7]   swap (3,4)
# 5   [1, 2, 3, 4, 5, 6, 7]   COMPLETE





"""
UPER:
U:
    > You have a list of numbers from 1 to n (n being the length of the list)
    > The numbers are scrambled
    > Return how many swaps are needed to put back in order

P:
    > find the first number out of order (first)
    > find the second number out of order (second)
    > put the second number where the first number belongs (if its not already there)
    > continue to the next number out of order

"""

arr = [7, 1, 3, 2, 4, 5, 6]

def minimumSwaps(arr):
    # print(arr)
    first = None
    second = None
    swapped = 0
    inPlace = [False for i in range(len(arr))]
    print(inPlace)
    print('start: ', arr)
    while(False in inPlace):
        for i in range(len(arr)):
            if arr[i] == i+1:
                print('in its place: ', arr[i])
                inPlace[i] = True

            else:
                # not in place
                first = arr[i]
                
                # find what number first is taking its position
                for j in range(len(arr)):
                    if arr[j] == i+1 :
                        # swap with index of first number
                        # print('arr[j]', arr[j])
                        # print('i+1', i+1)
                        if arr[j] != arr[first-1]:
                            arr[j], arr[first-1] = arr[first-1], arr[j]
                            print('\t', arr[j])
                            print('\t', arr[first-1])
                            print('swapped1: ', arr)
                            swapped += 1
                        arr[i], arr[first-1] = arr[first-1], arr[i]
                        print('\t', arr[i])
                        print('\t', arr[first-1])
                        print('swapped2: ', arr)
                        swapped += 1
        print("Finished: ", arr)
        print("Finished: ", inPlace)
        print("Swapped Count: ", swapped)

minimumSwaps(arr)