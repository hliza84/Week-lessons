"""1. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
Person  Relation
Darth Vader father
Leia    sister
Han brother in law
R2D2    droid
Examples
relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
relation_to_luke("Leia") ➞ "Luke, I am your sister."
relation_to_luke("Han") ➞ "Luke, I am your brother in law."
"""

str = input("Enter your name")
if str == "Darth Vader":
    print("Luke, I am your father.")
elif str == "Leia":
    print("Luke, I am your sister.")
elif str == "Han":
    print("Luke, I am your brother in law.")
elif str == "R2D2":
    print("Luke, I am your droid.")
else:
    print("I'm not your relation")
"""2. Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.
Examples
damage(40, 5, "second") ➞ 200
damage(100, 1, "minute") ➞ 6000
damage(2, 100, "hour") ➞ 720000
Notes
Return "invalid" if damage or speed is negative.
"""
l = [(40, 5, "second"), (100, 1, "minute"),
     (2, 100, "hour")]
for i, j, k in l:
    if k == "second":
        result = i*j
    elif k == "minute":
        result = i*j*60
    elif k == "hour":
        result = i*j*3600
    print(result)
"""3. Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
filter_list(["Nothing", "here"]) ➞ []
"""
lst = ["Nothing", "here"]
lst1 = []
for i in lst:
    if isinstance(i, int):
        lst1.append(i)

print(lst1)

"""4. Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.
Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
is_symmetrical(1112111) ➞ True
"""
num = input("Enter a number")
if num == num[::-1]:

    print("True")
else:
    print("False")

"""5. Create a function that changes all the elements in a list as follows:
Add 1 to all even integers, nothing to odd integers.
Concatenates "!" to all strings and make the first letter of the word a capital letter.
Changes all boolean values to its opposite.
Examples
change_types(["a", 12, True]) ➞ ["A!", 13, False]
change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]
change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]
Notes
There won't be any float values.
You won't get strings with both numbers and letters in them.
Although the task may be easy, try keeping your code as clean and as readable as possible!
    """
lst = [13, "13", "12", "twelve"]
lst1 = []
for i in lst:
    if isinstance(i, int) and i % 2 == 0:
        i += 1
        lst1.append(i)
    elif isinstance(i, str):
        s = i.capitalize()+"!"
        lst1.append(s)
    elif isinstance(i, bool):
        b = not i
        lst1.append(b)
    else:
        lst1.append(i)
print(lst1)
"""6. Create a function that takes a string s and returns a list of two-paired characters. If the string has an odd number of characters, add an asterisk * in the final pair.
See the below examples for a better understanding:
Examples
string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]
string_pairs("edabit") ➞ ["ed", "ab", "it"]
string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]
Notes
Return [] if the given string is empty."""
s = "abcge"
if len(s) % 2 == 1:
    s += '*'
lst = []
for i in range(0, len(s), 2):
    lst.append(s[i:i+2])
print(lst)
"""7. Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.
Examples
stupid_addition(1, 2) ➞ "12"
stupid_addition("1", "2") ➞ 3
stupid_addition("1", 2) ➞ None
Notes
If the two parameters are different data types, return None.
All parameters will either be strings or integers."""
s = [(1, 2)]
result = []
for i, j in s:
    if isinstance(i, str) and isinstance(j, str):
        result.append(i + j)
    elif isinstance(i, int) and isinstance(j, int):
        result.append(str(i) + str(j))
    else:
        result = None
print(result)
"""8. Write a function that does the following operations: adding, subtracting, dividing, or multiplying values. It is simply referred to as variable operation variable. Of course, the variables have to be defined, but in this challenge the variables will be defined for you. All you have to do is look at the variables, do some string to integer conversions, use some if conditionals, and combine them based on the operation.
The numbers and operation will be given as strings, and you should return the value as a string as well.
Examples
operation("1", "2", "add" ) ➞ "3"
operation("4", "5", "subtract") ➞ "-1"
operation("6", "3", "divide") ➞ "2"
Notes
The numbers and operation will be given as strings, and you should also return the value as a string.
If the answer is "undefined", return "undefined" (e.g. dividing by zero).
For divide, go ahead and round down to an integer."""
l = [("2", "3", "add"), ("5", "2", "subtract"),
     ("10", "5", "divide"), ("3", "4", "multiply")]
for i, j, k in l:
    if k == "add":
        result = int(i) + int(j)
    elif k == "subtract":
        result = int(i) - int(j)
    elif k == "divide":
        result = int(i) / int(j)
    elif k == "multiply":
        result = int(i) * int(j)
    else:
        result = None
    print(result)
"""9. Check if the given string consists of only letters and spaces and if every letter is in lower case.
Examples
letters_only("PYTHON") ➞ False
letters_only("python") ➞ True
letters_only("12321313") ➞ False
letters_only("i have spaces") ➞ True
letters_only("i have numbers(1-10)") ➞ False
letters_only("") ➞ False
Notes
Empty arguments will always return False.
Input values will be mixed (symbols, letters, numbers)."""
s = input("Enter anything")
if all(i.islower() or i.isspace() for i in s):
    print("True")
else:
    print("False")
"""
10. Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.
Examples
check([1, 2, 3]) ➞ "increasing"
check([3, 2, 1]) ➞ "decreasing"
check([1, 2, 1]) ➞ "neither"
check([1, 1, 2]) ➞ "neither"
Notes
The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater than the 0-indexed 1.
Input lists have a minimum length of 2.
"""
lst = [3, 2, 1]
increasing = True
decreasing = True

for i in range(len(lst) - 1):
    if lst[i] >= lst[i+1]:
        increasing = False
    if lst[i] <= lst[i+1]:
        decreasing = False

if increasing:
    print("increasing")
elif decreasing:
    print("decreasing")
else:
    print("neither")
