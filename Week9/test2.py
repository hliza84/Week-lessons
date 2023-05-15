"""1.Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.

The criteria for a candidate to be qualified in the coding interview is:

The candidate should have complete all the questions.
The maximum time given to complete the interview is 120 minutes.
The maximum time given for very easy questions is 5 minutes each.
The maximum time given for easy questions is 10 minutes each.
The maximum time given for medium questions is 15 minutes each.
The maximum time given for hard questions is 20 minutes each.
If all the above conditions are satisfied, return "qualified", else return "disqualified".

You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.

Given a list , in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].

The maximum time to complete the interview includes a buffer time of 20 minutes.

Examples
interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ "qualified"

interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞  "qualified"

interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ "disqualified"
# Exceeded the time limit for a medium question.

interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ "disqualified"
# Did not complete all the questions.
    """


# def interview(task_list, total):
#     if len(task_list) != 8:
#         return "disqualified"
#     if sum(task_list) > total - 20:
#         return "disqualified"
#     for i in range(len(task_list)):
#         if i < 2 and task_list[i] > 5:
#             return "disqualified"
#         elif i < 4 and task_list[i] > 10:
#             return "disqualified"
#         elif i < 6 and task_list[i] > 15:
#             return "disqualified"
#         elif task_list[i] > 20:
#             return "disqualified"
#     return "qualified"


# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))

"""2.In abstract set theory, a construction due to von Neumann represents the natural numbers by sets, as follows:

0 = [ ] is the empty set
1 = 0 ∪ [ 0 ] = [ 0 ] = [ [ ] ]
2 = 1 ∪ [ 1 ] = [ 0, 1 ] = [ [ ], [ [ ] ] ]
n = n−1 ∪ [ n−1 ] = ...
Write a function that receives an integer n and produces the representing set.

Examples
rep_set(0) ➞ []

rep_set(1) ➞ [[]]

rep_set(2) ➞ [[], [[]]]

rep_set(3) ➞ [[], [[]], [[], [[ ]]]]
"""


# def rep_set(n):
#     if n == 0:
#         return []
#     else:
#         prev_set = rep_set(n-1)
#         return prev_set + [prev_set.copy()]


# print(rep_set(5))

"""3.Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

For example:

"15 // 0"  ➞ -1
Examples
arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1
    """


# def arithmetic_operation(s):
#     parts = s.split()
#     num1 = int(parts[0])
#     num2 = int(parts[2])
#     op = parts[1]

#     if op == '+':
#         return num1 + num2
#     elif op == '-':
#         return num1 - num2
#     elif op == '*':
#         return num1 * num2
#     elif op == '//':
#         if num2 == 0:
#             return -1
#         else:
#             return num1 // num2


# print(arithmetic_operation("12 * 12"))

"""4.Create a function that takes a string as an argument and returns the Morse code equivalent.

Examples
encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"
This dictionary can be used for coding:


    """


# def encode_morse(message):
#     char_to_dots = {
#         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#         'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#         '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#         '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#         ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#         '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
#     }

#     message = message.upper()
#     morse_code = ''
#     for char in message:
#         if char in char_to_dots:
#             morse_code += char_to_dots[char] + ' '
#     return morse_code.strip()


# print(encode_morse("This dictionary"))

"""5.Your goal is to create a function that returns a list with a string for each of the 108 tiles in the following format:

"rank suit"
Where rank is a number from 1 to 9 and suit is one of the three suits (tong, tiao, wan), both written in the pinyin transcription of Mandarin Chinese (for numbers see table below).

Number	Character	Pinyin
1	一	yi
2	二	er
3	三	san
4	四	si
5	五	wu
6	六	liu
7	七	qi
8	八	ba
9	九	jiu
Three of the tiles have special names. Each of the 4 copies of these tiles should be represented by their names only (no suit, no rank):

One of tong is called bing gan (饼干, cookie)
Two of tong is called yan jing (眼镜, glasses)
One of tiao is called ji (鸡, chicken)
Examples of tiles
Five of tong ➞ "wu tong"

Seven of wan ➞ "qi wan"

One of tiao ➞ "ji"

Three of tiao ➞ "san tiao"""
# def gen_tiles():
#     suits = ['tong', 'tiao', 'wan']
#     rank = ['yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
#     tiles = []
#     for i in suits:
#         for j in rank:
#             x = ''
#             if i == 'tong' and j == 'yi':
#                 x = 'bing gan'
#             elif i == 'tiao' and j == 'yi':
#                 x = 'ji'
#             elif i == 'tong' and j == 'er':
#                 x = 'yan jing'
#             else:
#                 x = j + ' ' + i
#             for k in range(4):
#                 tiles.append(x)
#     return tiles


# print(gen_tiles(Three of tiao))

"""6.Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.

Examples
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True
"""


# def consecutive_combo():
#     lst_1 = [1, 4, 5, 6]
#     lst_2 = [2, 3, 7, 8, 10]
#     x = sorted(lst_1)
#     y = sorted(lst_2)
#     z = x+y
#     z.sort()
#     for i in range(1, len(z)):
#         if z[i]-z[i-1] != 1:
#             return False
#     else:
#         return True


# print(consecutive_combo())

"""7.A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of the tallest building is 4 (second-most right column).

[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]
Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.
"""
# matrix = [[0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 1, 0],
#           [0, 0, 1, 0, 1, 0],
#           [0, 1, 1, 1, 1, 0],
#           [1, 1, 1, 1, 1, 1]]


# def tallest_skyscraper(matrix):
#     max_height = 0

#     for j in range(len(matrix[0])):
#         height = 0
#         for i in range(len(matrix)):
#             if matrix[i][j] == 1:
#                 height += 1
#         max_height = max(max_height, height)

#     return max_height


# print(tallest_skyscraper(matrix))

"""8.Given a list of integers representing the color of each sock, determine how many pairs of socks with matching colors there are. For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

Create a function that returns an integer representing the number of matching pairs of socks that are available.

Examples
sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3
    """
# lst = [10, 20, 20, 10, 10, 30, 50, 10, 20]


# def sock_merchant(lst):
#     pairs = 0
#     for i in enumerate(lst):
#         if lst[i] == lst[i+n]:
#             pairs += 1
#             lst.remove(i, i+n)
#             continue
#         return pairs


"""9.Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.

Examples
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []
    """


# def remove_letters(lst, string):
#     for char in string:
#         if char in lst:
#             lst.remove(char)
#     return lst


# print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))

"""10.Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).

Examples
majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
    """


# def majority_vote(lst):
#     new_lst = []
#     data_len = len(lst)
#     for i in range(data_len):
#         for j in range(i+1, data_len+2):
#             if lst[i] != lst[j]:
#                 lst.remove(lst[i])
#     return lst


# print(majority_vote(["A", "A", "A", "B", "C", "A"]))

# def majority_vote(lst):
#     data_len = len(lst)
#     i = 0
#     while i < len(lst):
#         j = i + 1
#         while j < len(lst):
#             if lst[i] != lst[j]:
#                 lst.remove(lst[j])
#             else:
#                 j += 1
#         if lst.count(lst[i]) <= data_len / 2:
#             lst.remove(lst[i])
#         else:
#             i += 1

#     if len(lst) > 0:
#         return lst[0]
#     else:
#         return None
# այս խնդրի լուծման այլ տարբերակ բայց 2ն էլ չեմ հասկացել

# def majority_vote(lst):
#     for i in set(lst):

#         if lst.count(i) > len(lst)//2:
#             return i

#     return None


# print(majority_vote(["A", "A", "A", "B", "C", "A"]))

"""11.Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
    """


# def pluralize(lst):
#     new_lst = set()
#     for i in set(lst):
#         if lst.count(i) > 1:
#             new_lst.add(i+"s")
#         else:
#             new_lst.add(i)
#     return new_lst


# print(pluralize(["table", "table", "table"]))


"""12.Write a function that takes the coordinates of three points in the form of a 2d array and returns the perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.

Examples
perimeter([[15, 7], [5, 22], [11, 1]]) ➞ 47.08

perimeter([[0, 0], [0, 1], [1, 0]]) ➞ 3.41

perimeter([[-10, -10], [10, 10 ], [-10, 10]]) ➞ 68.28
Notes
The given points always create a triangle.
The numbers in the argument array can be positive or negative.
Output should have 2 decimal places
This challenge is easier than it looks.
"""


# def perimeter(a, b, c):
#     ab = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
#     bc = ((b[0]-c[0])**2 + (b[1]-c[1])**2)**0.5
#     ac = ((a[0]-c[0])**2 + (a[1]-c[1])**2)**0.5
#     perim = round(ab + bc + ac, 2)
#     return perim


# print(perimeter([15, 7], [5, 22], [11, 1]))

"""13.Count and Identify Data Types
Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.

List order is:

[int, str, bool, list, tuple, dictionary]
Examples
count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]

count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]

count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]

count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]
Notes
If no arguments are given, return [0, 0, 0, 0, 0, 0]
    """


# def count_datatypes(*args):
#     lst = [type(i) for i in args]
#     return [lst.count(i) for i in (int, str, bool, list, tuple, dict)]


# print(count_datatypes("Hello", "Bye", True, True, False, {
#       "1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23))
"""14.There are many different styles of music and many albums exhibit multiple styles. Create a function that takes a list of musical styles from albums and returns how many styles are unique.

Examples
unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
]) ➞ 9

unique_styles([
  "Soul",
  "House,Folk",
  "Trance,Downtempo,Big Beat,House",
  "Deep House",
  "Soul"
]) ➞ 7
    """


def unique_styles(albums):
    unique_styles_set = set()
    for album in albums:
        styles = album.split(',')
        unique_styles_set.update(styles)
    return len(unique_styles_set)


print(unique_styles([
    "Soul",
    "House,Folk",
    "Trance,Downtempo,Big Beat,House",
    "Deep House",
    "Soul"
]))
