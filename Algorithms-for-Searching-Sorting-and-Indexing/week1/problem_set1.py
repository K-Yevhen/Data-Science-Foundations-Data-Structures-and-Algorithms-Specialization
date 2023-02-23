# Problem 1: Find Crossover Indices.

# First write a "helper" function with two extra parameters
# left, right that ddedscribes the search region as shown below


def findCrossoverIndexHelper(x, y, left, right):
    # Note: Output index i such that
    #         left <= i <= right
    #         x[i] <= y[i]
    # First, Write down our invariants as assertions here
    assert (len(x) == len(y))
    assert (left >= 0)
    assert (left <= right - 1)
    assert (right < len(x))
    # Here is the key property we would like to maintain.
    assert (x[left] > y[left])
    assert (x[right] < y[right])

    # your code here
    if left > right:
        return None
    else:
        mid = (left + right) // 2

        if x[mid] > y[mid] and x[mid + 1] < y[mid + 1]:
            return mid

        elif x[mid] > y[mid]:
            return findCrossoverIndexHelper(x, y, mid + 1, right)

        else:
            return findCrossoverIndexHelper(x, y, left, mid - 1)


# Define the function findCrossoverIndex that wil
# call the helper function findCrossoverIndexHelper
def findCrossoverIndex(x, y):
    assert(len(x) == len(y))
    assert(x[0] > y[0])
    n = len(x)
    assert(x[n-1] < y[n-1]) # Note: this automatically ensures n >= 2 why?
    # your code here
    return findCrossoverIndexHelper(x, y, 0, len(x)-1)


# BEGIN TEST CASES
j1 = findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 5, 6, 7, 8, 9])
print('j1 = %d' % j1)
assert j1 == 1, "Test Case # 1 Failed"

j2 = findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 4.2, 4.3, 4.5, 8, 9])
print('j2 = %d' % j2)
assert j2 == 1 or j2 == 5, "Test Case # 2 Failed"

j3 = findCrossoverIndex([0, 1], [-10, 10])
print('j3 = %d' % j3)
assert j3 == 0, "Test Case # 3 failed"

j4 = findCrossoverIndex([0,1, 2, 3], [-10, -9, -8, 5])
print('j4 = %d' % j4)
assert j4 == 2, "Test Case # 4 failed"

print('Congratulations: all test cases passed - 10 points')
# END TEST CASES

# Problem 2 (Find integer cube root.)


def integerCubeRootHelper(n, left, right):
    cube = lambda x: x * x * x  # anonymous function to cube a number
    assert (n >= 1)
    assert (left < right)
    assert (left >= 0)
    assert (right < n)
    assert (cube(left) < n), f'{left}, {right}'
    assert (cube(right) > n), f'{left}, {right}'
    # your code here
    mid = (left + right) // 2
    if (cube(mid) <= n and cube(mid + 1) > n):
        return mid
    elif (cube(mid) > n):
        return integerCubeRootHelper(n, left, mid)  # Call 1
    else:
        return integerCubeRootHelper(n, mid, right)  # Call 2

# Write down the main function
def integerCubeRoot(n):
    assert( n > 0)
    if (n == 1):
        return 1
    if (n == 2):
        return 1
    return integerCubeRootHelper(n, 0, n-1)

assert(integerCubeRoot(1) == 1)
assert(integerCubeRoot(2) == 1)
assert(integerCubeRoot(4) == 1)
assert(integerCubeRoot(7) == 1)
assert(integerCubeRoot(8) == 2)
assert(integerCubeRoot(20) == 2)
assert(integerCubeRoot(26) == 2)
for j in range(27, 64):
    assert(integerCubeRoot(j) == 3)
for j in range(64,125):
    assert(integerCubeRoot(j) == 4)
for j in range(125, 216):
    assert(integerCubeRoot(j) == 5)
for j in range(216, 343):
    assert(integerCubeRoot(j) == 6)
for j in range(343, 512):
    assert(integerCubeRoot(j) == 7)
print('Congrats: All tests passed! (10 points)')

# Problem 3 (Develop Multiway Merge Algorithm, 15 points).

def twoWayMerge(lst1, lst2):
    # Implement the two way merge algorithm on
    #          two ascending order sorted lists
    # return a fresh ascending order sorted list that
    #          merges lst1 and lst2
    # your code here
    n1 = len(lst1)
    n2 = len(lst2)
    output_lst = []  # This is the list we will return
    i1 = 0
    i2 = 0
    while (i1 < n1 or i2 < n2):
        if i1 < n1 and i2 < n2:  # We are processing both lists
            if (lst1[i1] <= lst2[i2]):  # lst[i1] is the smaller elt
                output_lst.append(lst1[i1])  # append to end of output list
                i1 = i1 + 1  # advance index i1
            else:
                output_lst.append(lst2[i2])  # append to end of output list
                i2 = i2 + 1  # advance index i2
        elif i1 < n1:  # We have run past the end of lst2
            output_lst.append(lst1[i1])  # append lst1 to end of output list
            i1 = i1 + 1
        else:  # We have run past the end of lst1
            output_lst.append(lst2[i2])  # append lst2 to end of output list
            i2 = i2 + 1
    return output_lst

# given a list_of_lists as input,
#   if list_of_lists has 2 or more lists,
#        compute 2 way merge on elements i, i+1 for i = 0, 2, ...
#   return new list of lists after the merge
#   Handle the case when the list size is odd carefully.


def oneStepKWayMerge(list_of_lists):
    if (len(list_of_lists) <= 1):
        return list_of_lists
    ret_list_of_lists = []
    k = len(list_of_lists)
    for i in range(0, k, 2):
        if (i < k-1):
            ret_list_of_lists.append(twoWayMerge(list_of_lists[i], list_of_lists[i+1]))
        else:
            ret_list_of_lists.append(list_of_lists[k-1])
    return ret_list_of_lists

# Given a list of lists wherein each
#    element of list_of_lists is sorted in ascending order,
# use the oneStepKWayMerge function repeatedly to merge them.
# Return a single merged list that is sorted in ascending order.


def kWayMerge(list_of_lists):
    k = len(list_of_lists)
    if k == 1:
        return list_of_lists[0]
    else:
        new_list_of_lists = oneStepKWayMerge(list_of_lists)
        return kWayMerge(new_list_of_lists)

# BEGIN TESTS
lst1= kWayMerge([[1,2,3], [4,5,7],[-2,0,6],[5]])
assert lst1 == [-2, 0, 1, 2, 3, 4, 5, 5, 6, 7], "Test 1 failed"

lst2 = kWayMerge([[-2, 4, 5 , 8], [0, 1, 2], [-1, 3,6,7]])
assert lst2 == [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8], "Test 2 failed"

lst3 = kWayMerge([[-1, 1, 2, 3, 4, 5]])
assert lst3 == [-1, 1, 2, 3, 4, 5], "Test 3 Failed"

print('All Tests Passed = 15 points')
# END TESTS
