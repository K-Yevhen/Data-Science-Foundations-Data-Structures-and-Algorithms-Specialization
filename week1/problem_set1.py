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

