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

arr = [4, 3, 1, 2]

def minimumSwaps(arr):
    # print(arr)
    first = None
    second = None
    swapped = 0
    inPlace = [False for i in range(len(arr))]
    print(inPlace)
    print('start: ', arr)

    # create hashtable with key=number value=index
    cache = {}
    for i in range(len(arr)):
        cache[arr[i]] = i

    print(cache)


    while(False in inPlace):
        for i in range(len(arr)):
            if arr[i] == i+1:
                print('in its place: ', arr[i])
                inPlace[i] = True

            else:
                # not in place
                first = arr[i]

                # Find what number belongs in that index by pulling from cache
                # cache[i+1]
                # print(inPlace)
                # print(arr[cache[i+1]])
                # print(cache)
                # print(arr)
                if arr[cache[i+1]] != arr[first-1] :
                    print('cache before: ', cache)
                    print('arr before: ', arr)
                    print("\t", arr[cache[i+1]])
                    print("\t", arr[first-1])
                    
                    # swap numbers in the list
                    first_num = cache[i+1]
                    second_num = arr[first-1]
                    arr[cache[i+1]], arr[first-1] = arr[first-1], arr[cache[i+1]]
                    print("swapped1: ", arr)
                    # swap numbers in the cache
                    swapped += 1
                    cache[i+1], cache[second_num] = cache[second_num], cache[i+1]
                    print('cache after: ', cache)
                    print('arr after: ', arr)
                print('cache before: ', cache)
                print('arr before: ', arr)
                arr[i], arr[first-1] = arr[first-1], arr[i]
                cache[i+1], cache[first] = cache[first], cache[i+1]
                swapped += 1
                print("\t", arr[i])
                print("\t", arr[first-1])
                print("swapped2: ", arr)
                print('cache after: ', cache)
                print('arr after: ', arr)
        print("Finished: ", arr)
        print("Finished: ", inPlace)
        print("Swapped Count: ", swapped)
        print("should be: 3")

minimumSwaps(arr)