"""1. Create a function that takes a string and returns it as an integer.
Examples
"6" ➞ 6
"1000" ➞ 1000
Notes
All numbers will be whole.
All numbers will be positive.
    """
string = "55"
result = int(string)
print(result)

"""2. Create a function that takes a boolean variable flag and returns it as a string.
Examples
True ➞ "True"
False ➞ "False"
    """
x = True
y = str(x)
print(y)

"""3. Write a function that returns the string "something" joined with a space " " and the given argument a.
Examples
"is better than nothing" ➞ "something is better than nothing"
"Bob Jane" ➞ "something Bob Jane"
"something" ➞ "something something"
"""
string = "something"
a = input("Enter anything")
x = string+" "+a
print(x)

"""4. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
Person  Relation
Darth Vader father
Leia    sister
Han brother in law
R2D2    droid
Examples
"Darth Vader" ➞ "Luke, I am your father."
"Leia" ➞ "Luke, I am your sister."
"Han" ➞ "Luke, I am your brother in law."
"""
name = input("Please, enter your name")
person = ("Darth Vader", "Leia", "Han", "R2D2")
relation = ("father", "sister", "brother in low", "droid")
x = slice(4)
result = (name == person[x])*("Luke, I am your"+str(relation[x]))
print(result)

"""5. Create a function that takes a string and returns the number (count) of vowels contained within it.
Examples
"Celebration" ➞ 5
"Palm" ➞ 1
"Prediction" ➞ 4
Notes
a, e, i, o, u are considered vowels (not y).
"""

txt = input("Enter  anything")
result = txt.count("a") + txt.count("e")+txt.count("i") + \
    txt.count("o")+txt.count("u")
print(result)

"""EXTRA Knowledge
6. Create a function that returns True if a given inequality expression is correct and False otherwise.
Examples
"3 < 7 < 11" ➞ True
"13 > 44 > 33 > 1" ➞ False
"1 < 2 < 6 < 9 > 3" ➞ True
"""
exp = "3 < 7 < 11 >15"
parts = exp.split()
a = parts[0]
b = parts[1]
c = parts[2]
d = parts[3]
e = parts[4]
f = parts[5]
result = eval(f"{a} {b} {c} {d} {e} {f}")

print(result)
exp = "3 < 7 < 11 >15"
eval(f"print{x}")

"""7. Create a function that replaces all the vowels in a string with a specified character.
Examples
"the aardvark", "#" ➞ "th# ##rdv#rk"
"minnie mouse", "?" ➞ "m?nn?? m??s?"
"shakespeare", "*" ➞ "sh*k*sp**r*"
"""
s = "Hello World"
vowels = "aeiouAEIOU"
result = s.translate(str.maketrans(vowels, "#" * len(vowels)))
print(result)

"""8. Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.
Examples
"1234123456785678" ➞ "************5678"
"8754456321113213" ➞ "************3213"
"35123413355523" ➞ "**********5523"
"""
card_number = input("Enter your card number")
closed = "*" * (len(card_number) - 4) + card_number[-4:]
print(closed)

"""9. Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.
Examples
"Donald Trump" ➞ "Trump Donald"
"Rosie O'Donnell" ➞ "O'Donnell Rosie"
"Seymour Butts" ➞ "Butts Seymour" 
"""
name = input("Enter your first name and last name, please")
first_name, last_name = name.split()
swapped_name = last_name+" "+first_name
print(swapped_name)

"""10. An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
Examples
"Algorism" ➞ True
"PasSword" ➞ False
# Not case sensitive.
"Consecutive" ➞ False
"""
word = input("Please, enter anything")
word = word.lower()
result = len(set(word)) == len(word)
print(result)

"""11.Create a function to test if a string is valid pin or not. a valid pin has only 4 or 6 characters, only numerical characters, no whitespace
    """
pin = input("Enter your pin")
result = "False"*(len(pin) != 4 and len(pin) != 6 and not pin.isdigit()) + \
    "True"*(len(pin) == 4 and len(pin) == 6 and pin.isdigit())
print(result)
