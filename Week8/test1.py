
"""1. Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.
(Hint: lambda will be passed to sort method's key parameter as argument)
Please check out Hint 0 below to be informed about a glitch regarding this exercise.
lst=[100, 10, 10000, 1, 9, 999, 99]
"""
lst = [100, 10, 10000, 1, 9, 999, 99]
lst.sort(key=lambda x: -x)
print(lst)

"""2. Using sorted() function, reverse parameter and lambda sort the tuples in the list based on the last character of the second items in reverse order.
lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
#Type your answer here.
Decorators, function inside function
    """
lst = [(19542209, "New York"), (4887871, "Alabama"), (1420491, "Hawaii"),
       (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]


def last_char_reverse(item):
    return item[1][-1]


sorted_lst = sorted(lst, key=lambda x: last_char_reverse(x), reverse=True)
print(sorted_lst)

"""
3. Write function which take a function as an input and run it and print how count how many times I have run the input provide functions.
"""
