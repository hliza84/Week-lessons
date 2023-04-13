"""





7. Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.
Examples
hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"
hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"
hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"
Notes
In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0, and "s"s with 5.
8. Create a function that takes an integer and returns it as an ordinal number. An Ordinal Number is a number that tells the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.
Examples
return_end_of_number(553) ➞ "553-RD"
return_end_of_number(34) ➞ "34-TH"
return_end_of_number(1231) ➞ "1231-ST"
return_end_of_number(22) ➞ "22-ND"
return_end_of_number(412) ➞ "412-TH"
9. Create a function that converts Celsius to Fahrenheit and vice versa.
Examples
convert("35*C") ➞ "95*F"
convert("19*F") ➞ "-7*C"
convert("33") ➞ "Error"
Notes
Round to the nearest integer.
If the input is incorrect, return "Error".
For the formulae to convert back and forth, check the Resources tab.
10. Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:
Original    Complement
"AAA" "UUU"
"UUU" "AAA"
"GGG" "CCC"
"CCC" "GGG"
Your function should find the complement on the right AND also reverse the resulting string.
Examples
reverse_complement("GUGU") ➞ "ACAC"
reverse_complement("UCUCG") ➞ "CGAGA"
reverse_complement("CAGGU") ➞ "ACCUG"
Notes
You can assume all input seqeuences will be valid.
11. Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.
eval() is not allowed. In case of division, whenever the second number equals "0" return -1.
For example:
"15 // 0"  ➞ -1
Examples
arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24
arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0
arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144
arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1
Notes
All the inputs are only integers.
The operators are * - + and //.
Hint: Think about the single space that appears before and after the arithmetic operator.

"""
"""1. Write a function that takes a string name and a number num (either 0 or 1) and return "Hello" + name if num is 1, otherwise return "Bye" + name.
Examples
say_hello_bye("alon", 1) ➞ "Hello Alon"
say_hello_bye("Tomi", 0) ➞ "Bye Tomi"
say_hello_bye("jose", 0) ➞ "Bye Jose"
"""


# def say_hello_bye(name, num):
#     if num == 1:
#         return f"Hello {name.title()}"
#     else:
#         return f"Bye {name.title()}"
# print(say_hello_bye("jose", 0))

"""2. Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise. The list will contain 4 elements.
Examples
test_jackpot(["@", "@", "@", "@"]) ➞ True
test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True
test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True
test_jackpot(["&&", "&", "&&&", "&&&&"]) ➞ False
test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False
"""


# def test_jackpot(result):
#     if len(set(result)) == 1:
#         return True
#     else:
#         return False

# print(test_jackpot(["&&", "&", "&&&", "&&&&"]))

"""3. Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler can clear all the hurdles.
A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.
Examples
hurdle_jump([1, 2, 3, 4, 5], 5) ➞ True
hurdle_jump([5, 5, 3, 4, 5], 3) ➞ False
hurdle_jump([5, 4, 5, 6], 10) ➞ True
hurdle_jump([1, 2, 1], 1) ➞ False
Notes
Return True for the edge case of an empty array of hurdles. (Zero hurdles means that any jump height can clear them).
    """
# def hurdle_jump(hurdles, jump):
#     for hurdle in hurdles:
#         if hurdle > jump:
#             return False
#     return True
# print(hurdle_jump([1, 2, 3, 4, 5], 5))

"""4. Create a function that takes a number as its argument and returns a list of all its factors.
Examples
factorize(12) ➞ [1, 2, 3, 4, 6, 12]
factorize(4) ➞ [1, 2, 4]
factorize(17) ➞ [1, 17]
Notes
The input integer will be positive.
A factor is a number that evenly divides into another number without leaving a remainder. The second example is a factor of 12, because 12 / 2 = 6, with remainder 0.
"""

# def factorize(num):
#     factors = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             factors.append(i)
#     return factors

# print(factorize(17))
"""5. Create a function that returns the number of palindrome numbers in a specified range (inclusive).
For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33. Between 1550 and 1552 there is exactly one palindrome: 1551.
Examples
count_palindromes(1, 10) ➞ 9
count_palindromes(555, 556) ➞ 1
count_palindromes(878, 898) ➞ 3
Notes
A palindrome number is a number which remains the same when its digits are reversed. For example, 2552 reversed is still 2552. The reflectional symmetry of this number makes it a palindromic number.
Single-digit numbers are trivially palindrome numbers.
    """


# def count_palindromes(start, end):
#     count = 0
#     for num in range(start, end+1):
#         if str(num) == str(num)[::-1]:
#             count += 1
#     return count


# print(count_palindromes(555, 556))
"""6. Write a function that takes a string, breaks it up and returns it with vowels first, consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants.
Examples
split("abcde") ➞ "aebcd"
split("Hello!") ➞ "eoHll!"
split("What's the time?") ➞ "aeieWht's th tm?"
Notes
Vowels are a, e, i, o, u.
Define a separate is_vowel() function for easier to read code (recommendation).
    """


def split(string):
    vowels = []
    consonants = []
    for char in string:
        if char.lower() in 'aeiou':
            vowels.append(char)
        else:
            consonants.append(char)
    return ''.join(vowels + consonants)


print(split("Hello!"))
