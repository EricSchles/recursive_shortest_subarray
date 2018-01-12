import random
set_of_ints = set([1,2,3])
random_arr = [random.randint(0,20) for _ in range(40)]

# given a set of integers
# and an array of random integers
# find the shortest continous subarray that contains all the values from the set
def find_subarray(random_arr, set_of_ints):
    if len(random_arr) == len(set_of_ints):
        if set(random_arr) == set_of_ints:
            return random_arr
        else:
            return None
    elif (random_arr[0] in set_of_ints) and (random_arr[-1] in set_of_ints):
        arr = set(random_arr)
        if set_of_ints.issubset(arr):
            return random_arr
    else:
        if random_arr[0] in set_of_ints:
            return find_subarray(random_arr[:-1], set_of_ints)
        elif random_arr[-1] in set_of_ints:
            return find_subarray(random_arr[1:], set_of_ints)
        else:
            return find_subarray(random_arr[1:-1], set_of_ints)

print(find_subarray(random_arr, set_of_ints))
