"""1. Given a list, rotate the values clockwise by one (the last value is sent to the first position).
Check the examples for a better understanding.
Examples
[1, 2, 3, 4, 5] ➞ [5, 1, 2, 3, 4]
[6, 5, 8, 9, 7] ➞ [7, 6, 5, 8, 9]
[20, 15, 26, 8, 4] ➞ [4, 20, 15, 26, 8]
"""
lst = [1, 2, 3, 4, 5, 6]
lst.insert(0, lst.pop())
print(lst)

"""2. Create a function that inverts the rgb values of a given tuple.
Examples
color_invert((255, 255, 255)) ➞ (0, 0, 0)
# (255, 255, 255) is the color white.
# The opposite is (0, 0, 0), which is black.
color_invert((0, 0, 0)) ➞ (255, 255, 255)
color_invert((165, 170, 221)) ➞ (90, 85, 34)
Notes
Must return a tuple.
255 is the max value of a single color channel.
        """
col_inv = (0, 2, 3)
col_opp = (255-col_inv[0], 255-col_inv[1], 255-col_inv[2])
print(col_opp)

"""3. Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the list, return -1.
Examples
find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2
find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
find_bob(["Jimmy", "Layla", "James"]) ➞ -1
Notes
Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob").
        """
names = ["Bob", "Jimmy", "Layla"]
find_bob = (("Bob" not in names) *
            (-1) + (names.index("Bob")*("Bob" in names)))
print(find_bob)

"""EXTRA Knowledge
4. Given a list of numbers, write a function that returns a list that...
Has all duplicate elements removed.
Is sorted from least to greatest value.
Examples
unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7] """

unique_sort = [1, 4, 4, 4, 4, 4, 3, 2, 1, 2]
new_lst = sorted(set(unique_sort))
print(new_lst)

"""EXTRA Knowledge
5. Given two strings, create a function that returns the total number of unique characters from the combined string.
Examples
count_unique("apple", "play") ➞ 5
# "appleplay" has 5 unique characters:
# "a", "e", "l", "p", "y"
"sore", "zebra" ➞ 7
"a", "soup" ➞ 5"""
str1 = input("Enter any word")
str2 = input("Enter another word")
count_unique = len(set(str1) | set(str2))
print(count_unique)

"""6. Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.
Examples
{
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
} ➞ ["Becky", "John", "Steve"]
        """
stud_dict = {

    "Student 1": "Liza",
    "Student 2": "Sophie",
    "Student 3": "Vika",
    "Student 4": "Elza",
    "Student 5": "Narek",
    "Student 6": "Tigran"
}
names = sorted(stud_dict.values())
print(names)

"""7. Create a function that returns a list of strings sorted by length in ascending order.
Examples
sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
sort_by_length([]) ➞ []
Notes
Strings will have unique lengths, so don't worry about comparing two strings with identical length.
Return an empty array if the input array is empty"""

lst = ["may", "april", "september", "august"]
print(sorted(lst, key=len))

"""8. Write a function that converts a dictionary into a list of keys-values tuples.
Examples
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]
dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]"""

dict = {
    "D": 1,
    "B": 2,
    "C": 3
}
lst = dict.items()
print(lst)
"""9. Print the value of key "history" from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
"""
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
x = sampleDict.get("class").get("student").get("marks").get("history")
print(x)

"""10. Rename key of a dictionary
Write a program to rename a key city to a location in the following dictionary.
Given:
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Expected output:
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
    """
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)
