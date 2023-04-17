
"""1. Create a function which returns the number of true values there are in an array.
Examples
countTrue([true, false, false, true, false]) ➞ 2
countTrue([false, false, false, false]) ➞ 0
countTrue([]) ➞ 0
Notes
Return 0 if given an empty array.
All array items are of the type bool (true or false).
    """


def count_true_false(arr):
    true_count = 0
    false_count = 0
    for item in arr:
        if item:
            true_count += 1
        else:
            false_count += 1
    return (true_count, false_count)


arr = []
print(count_true_false(arr))


"""2.Create a function that validates whether a number n is within the bounds of lower and upper. Return false if n is not an integer.
Examples
intWithinBounds(3, 1, 9) ➞ true
intWithinBounds(6, 1, 6) ➞ false
intWithinBounds(4.5, 3, 8) ➞ false
Notes
The term "within bounds" means a number is considered equal or greater than a lower bound and lesser (but not equal) to an upper bound, (see example #2).
Bounds will be always given as integers.
    """


def intWithinBounds(n, lower, upper):
    if type(n) != int:
        return False
    if lower < n < upper:
        return True
    else:
        return False


print(intWithinBounds(4.5, 3, 8))
"""3. Create a function that takes three values:
h hours
m minutes
s seconds
Return the value that's the longest duration.
Examples
longestTime(1, 59, 3598) ➞ 1
longestTime(2, 300, 15000) ➞ 300
longestTime(15, 955, 59400) ➞ 59400
    """


def longest_time(h, m, s):
    max_duration = max(h, m/60, s/3600)
    if max_duration == h:
        return h
    elif max_duration == m/60:
        return m
    else:
        return s


print(longest_time(15, 955, 59400))

"""4. Create a function that takes the month and year (as integers) and returns the number of days in that month.
Examples
days(2, 2018) ➞ 28
days(4, 654) ➞ 30
days(2, 200) ➞ 28
days(2, 1000) ➞ 28
Notes
Don't forget about leap years!"""


def days(month, year):
    days_in_month = {
        1: 31,
        2: 28 if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) else 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return days_in_month[month]


print(days(2, 2018))
"""5. Create a function that takes a string and censors words over four characters with *.
Examples
censor("The code is fourty") ➞ "The code is ******"
censor("Two plus three is five") ➞ "Two plus ***** is five"
censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
Notes
Don't censor words with exactly four characters.
If all words have four characters or less, return the original string.
The amount of * is the same as the length of the word."""

text = input("Enter a string: ")


def censor(text):
    words = text.split()
    for i, word in enumerate(words):
        if len(word) > 4:
            words[i] = '*' * len(word)
    return ' '.join(words)


print(censor(text))

"""6. Given a sentence, create a function that replaces every "a" as an article with "an absolute". It should return the same string without any change if it doesn't have any "a".
Examples
absolute("I am a champion!!!") ➞ "I am an absolute champion!!!"
absolute("Such an amazing bowler.") ➞ "Such an amazing bowler."
absolute("A man with no haters.") ➞ "An absolute man with no haters."
Notes
Watch for uppercase letters as shown in example #3.
    """


sentence = input("Enter a sentence: ")


def absolute(sentence):
    return sentence.replace(" a ", " an absolute ").replace(" A ", " An absolute ")


print(absolute(sentence))

"""7. Return an Array of Subarrays
Write a function that takes three arguments (x, y, z) and returns an array containing x subarrays (e.g. [[], [], []]), each containing y number of item z.
x Number of subarrays contained within the main array.
y Number of items contained within each subarray.
z Item contained within each subarray.
Examples
matrix(3, 2, 3) ➞ [[3, 3], [3, 3], [3, 3]]
matrix(2, 1, "edabit") ➞ [["edabit"], ["edabit"]]
matrix(3, 2, 0) ➞ [[0, 0], [0, 0], [0, 0]]
Notes
The first two arguments will always be integers.
The third argument is either a string or an integer.
    """


def matrix(x, y, z):
    result = []
    for i in range(x):
        sublist = []
        for j in range(y):
            sublist.append(z)
        result.append(sublist)
    return result


print(matrix(2, 1, 3))

"""8. Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples
multiplyNums("2, 3") ➞ 6
multiplyNums("1, 2, 3, 4") ➞ 24
multiplyNums("54, 75, 453, 0") ➞ 0
multiplyNums("10, -2") ➞ -20
Notes
Bonus: Try to complete this challenge in one line!
    """
nums = "2, 3"


def multiplyNums(nums):
    num_list = nums.split(", ")
    product = 1
    for num in num_list:
        product *= int(num)
    return product


print(multiplyNums(nums))

"""9. Create a function that takes a string road and returns the car that's in first place. The road will be made of "=", and cars will be represented by letters in the alphabet.
Examples
firstPlace("====b===O===e===U=A==") ➞ "A"
firstPlace("e==B=Fe") ➞ "e"
firstPlace("proeNeoOJGnfl") ➞ "l"
Notes
Return "No car available" if there is no car on the road and "No road available" if there is no road.
    """


def firstPlace(str):
    if not str:
        return "No road available"
    cars = []
    for i in str:
        if i != '=':
            cars.append(i)
    if not cars:
        return "No car available"
    return cars[-1]


road = "proeNeoOJGnfl"
print(firstPlace(road))

"""
10. Create a function that takes an array of numbers between 1 and 10 (excluding one number) and returns the missing number.
Examples
missingNum([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missingNum([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
Notes
The array of numbers will be unsorted (not in order).
Only one number will be missing.
"""


def missing_Num(arr):
    arr.sort()
    arr_1 = range(1, 11)
    for i, j in zip(arr, arr_1):
        if i != j:
            return j


print(missing_Num([10, 5, 1, 2, 4, 6, 8, 3, 9]))
