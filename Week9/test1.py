"""Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.
    """


def arithmetic_operation(s):
    parts = s.split()
    num1 = int(parts[0])
    num2 = int(parts[2])
    op = parts[1]

    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '//':
        if num2 == 0:
            return -1
        else:
            return num1 // num2


"""A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.
is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True
    """


def is_disarium(n):
    s = str(n)
    total = 0
    for i in range(len(s)):
        digit = int(s[i])
        total += digit**(i+1)

    return total == n


"""Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:

# = 5
O = 3
X = 1
! = -1
!! = -3
!!! = -5
#s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.
A list of lists containing 2

If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.
    """

dict = {
    "#": 5,
    "O": 3,
    "X": 1,
    "!": -1,
    "!!": -3,
    "!!!": -5
}


def check_score(input_list):
    return sum([dict[j] for i in input_list for j in i])


print(check_score([
    ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
    ["!!!", "!!!", "!!", "!!", "!", "!", "X",
        "!", "!!!", "O", "!", "!!!", "X", "#"],
    ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
    ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
    ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
    ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!",
     "X", "O", "!", "#", "!!", "!!", "!!!"],
    ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
    ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
    ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
    ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
    ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
    ["!", "!!!", "!!", "X", "!!", "!!", "#",
        "!!!", "O", "!!", "!!!", "!", "!", "!"],
    ["!!!", "!!!", "!!", "O", "!", "!", "!!!",
     "!!!", "!!", "!!", "X", "!", "#", "#"],
    ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
]))


"""Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string.

Examples
convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"

convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"
    """


def convert_to_hex(txt):
    hex_vals = []
    for char in txt:
        hex_val = hex(ord(char))[2:]
        hex_vals.append(hex_val)
    return ' '.join(hex_vals)


print(convert_to_hex("Big Boi"))


"""Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.

Example
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
    """


def uncensor(txt, vowels):
    txt_list = list(txt)
    vowels_list = list(vowels)
    new_txt = ""
    vowel_index = 0
    for i in txt_list:
        if i == "*":
            new_txt += vowels_list[vowel_index]
            vowel_index += 1
        else:
            new_txt += i
    return new_txt


print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))

"""Using markdown, it's possible to format links such as https://edabit.com/challenges, into something tidier like this. Notice how the text "Go to the challenges!" appears when hovering over the link.

This was achieved by using this code:

[this](https://edabit.com/challenges "Go to the challenges!")
Given the url, the new name and optionally the hover_text, return the tidied up hyperlink as a string.

Examples
tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!") ➞ "[this](https://edabit.com/challenges "Go to the challenges!")"


Notes
Supply double quotes for the hover text.
Keep in mind that some tests will not include an argument for hover_text.
    """


def tidy_link(url, name, hover_text=""):
    if hover_text:
        return f"[{name}]({url} \"{hover_text}\")"
    else:
        return f"[{name}]({url})"


print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))

"""Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
    """


def pluralize(lst):
    plural_lst = set()
    for word in set(lst):
        if lst.count(word) > 1:
            plural_lst.add(word + "s")
        else:
            plural_lst.add(word)
    return plural_lst


"""Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.

Examples
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]
    """


def remove_letters(lst, string):
    new_lst = list(string)

    for i in new_lst:
        if i in lst:
            lst.remove(i)
    return lst


print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))

"""Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.

Examples
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "
    """


def censor_string(txt, lst, char):
    txt_to_list = list(txt.split(" "))
    for i in range(len(txt_to_list)):
        if txt_to_list[i] in lst:
            txt_to_list[i] = char*len(txt_to_list[i])
    return ' '.join(txt_to_list)


print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))


def censor_string(txt, lst, char):
    words = txt.split()  # Split the string into a list of words
    for i in range(len(words)):
        if words[i] in lst:  # If the word is in the list, censor it
            words[i] = char * len(words[i])
    return ' '.join(words)


"""Create a function based on the input and output. Look at the examples, there is a pattern.

Examples
secret("p.one.two.three") ➞ "<p class='one two three'></p>"

secret("p.one") ➞ "<p class='one'></p>"

secret("p.four.five") ➞ "<p class='four five'></p>"
    """


def secret(txt):
    classes = txt.split('.')[1:]  # remove the first item, which is always 'p'
    class_str = ' '.join(classes)
    return f"<p class='{class_str}'></p>"


print(secret("p.one"))

"""Create a function which takes in an encoded string and returns a dictionary according to the following example:

Examples
parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}

parse_code("michael0smith004331") ➞ {
  "first_name": "michael",
  "last_name": "smith",
  "id": "4331"
}

parse_code("Thomas00LEE0000043") ➞ {
  "first_name": "Thomas",
  "last_name": "LEE",
  "id": "43"
}
    """


def parse_code(txt):
    parts = txt.split("000")
    return {
        "first_name": parts[0].lower().capitalize(),
        "last_name": parts[1].lower().capitalize(),
        "id": parts[2]
    }


""""Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.

Examples
loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"

loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

loves_me(1) ➞ "LOVES ME"
    """


def loves_me(n):
    phrases = ['Loves me', 'Loves me not']
    result = [phrases[i % 2] for i in range(n - 1)]
    result.append(result[-1].upper() + '!')
    return ', '.join(result)
