"""1.Given a class for a BasicPlan, write the classes for StandardPlan and PremiumPlan which have class attributes of the following:

BasicPlan	StandardPlan	Premium Plan
✓	           ✓	            ✓	      can_stream
✓	           ✓	            ✓	      can_download
✓	           ✓	            ✓	      has_SD
✓	           ✓	                      has_HD
✓	                                      has_UHD
1	           2	             4	       num_of_devices
$8.99	     $12.99	            $15.99	   price
Examples
BasicPlan.has_SD ➞ True

PremiumPlan.has_SD ➞ True

BasicPlan.has_UHD ➞ False

BasicPlan.price ➞ "$8.99"

PremiumPlan.num_of_devices ➞ 4
    """


import math


class StandardPlan:
    def __init__(self, can_stream, can_download, has_SD, has_HD, has_UHD, num_of_devices, price):
        self.can_stream = True
        self.can_download = True
        self.has_SD = True
        self.has_HD = True
        self.has_UHD = False
        self.num_of_devices = 2
        self.price = "$ 12.99"


class PremiumPlan:
    def __init__(self, can_stream, can_download, has_SD, has_HD, has_UHD, num_of_devices, price):
        self.can_stream = True
        self.can_download = True
        self.has_SD = True
        self.has_HD = False
        self.has_UHD = False
        self.num_of_devices = 4
        self.price = "$ 15.99"


"""2.Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PI*r^2) and getPerimeter() (2*PI*r) which give both respective areas and perimeter (circumference).

For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.

Examples
circy = Circle(11)
circy.getArea()

# Should return 380.132711084365

circy = Circle(4.44)
circy.getPerimeter()

# Should return 27.897342763877365
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return round(math.pi * (self.radius ** 2))

    def getPerimeter(self):
        return round(2 * math.pi * self.radius)


circy = Circle(11)
print(circy.getArea())

circy = Circle(4.44)
print(circy.getPerimeter())


"""3.Create a method in the Person class which returns how another person's age compares. Given the objects p1, p2 and p3, which will be initialised with the attributes name and age, return a sentence in the following format:

{other_person} is {older than / younger than / the same age as} me.

Examples
p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)
p1.compare_age(p2) ➞ "Joel is older than me."

p2.compare_age(p1) ➞ "Samuel is younger than me."

p1.compare_age(p3) ➞ "Lily is the same age as me."
    """


class Person:
    def __init__(self, name, age):
        self. name = name
        self. age = age

    def compare_age(self, other):
        if self.age < other.age:
            return f"{other.name} is older than me."
        elif self.age > other.age:
            return f"{other.name} is younger than me."
        else:
            self.age == other.age
            return f"{other.name} is same as me."


p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

print(p1.compare_age(p2))

"""4.Ones, Threes and Nines (Version #1)
Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class. You will make variables (self.ones, self.threes, self.nines) to do this.

Examples
n1 = ones_threes_nines(5)
n1.nines ➞ 0

n1.ones ➞ 5

n1.threes ➞ 1
Notes
Do not use the math module.
See version #2 of this series.
    """


class Ones_threes_nines:
    def __init__(self, num):
        self.ones = num//1
        self.threes = num//3
        self.nines = num//9


n1 = Ones_threes_nines(5)
print(n1.ones)

"""5.Create a class that takes the following four arguments for a particular football player:

name
age
height
weight
Also, create three functions for the class that returns the following strings:

get_age() returns "name is age age"
get_height() returns "name is heightcm"
get_weight() returns "name weighs weightkg"

Examples
 p1 = player("David Jones", 25, 175, 75)

 p1.get_age() ➞ "David Jones is age 25"
 p1.get_height() ➞ "David Jones is 175cm"
 p1.get_weight() ➞ "David Jones weighs 75kg"
    """


class Player():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height}cm"

    def get_weight(self):
        return f"{self.name} is {self.weight}kg"


p1 = Player("David Jones", 25, 175, 75)
print(p1.get_age())

"""6.Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

Form the fullname by simply joining the first and last name together, separated by a space.
Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.
Examples
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
emp_1.fullname ➞ "John Smith"

emp_2.email ➞ "mary.sue@company.com"

emp_3.firstname ➞ "Antony"
    """


class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_nane(self):
        return f"{self.first_name} {self.last_name}"

    def email(self):
        return f"{self.first_name.lower()}"+"."+f"{self.last_name.lower()}@company.com"


emp_1 = Employee("John", "Smith")
print(emp_1.email())

"""7.
Create a class named User and create a way to check the number of users (number of instances) that were created, so that the value can be accessed as a class attribute.

Examples
u1 = User("johnsmith10")
User.user_count ➞ 1

u2 = User("marysue1989")
User.user_count ➞ 2

u3 = User("milan_rodrick")
User.user_count ➞ 3
Make sure that the usernames are accessible via the instance attribute username.

u1.username ➞ "johnsmith10"

u2.username ➞ "marysue1989"

u3.username ➞ "milan_rodrick"
    """
# xndri pahajy chem haskacel


class User:
    user_count = 0

    def __init__(self, username):
        self.username = username
        User.user_count += 1


u2 = User("marysue1989")
print(User.user_count)
"""8.Name Classes
Write a class called Name and create the following attributes given a first name and last name (as fname and lname):

An attribute called fullname which returns the first and last names.
An attribute called initials which returns the first letters of the first and last name. Put a . between the two letters.
Remember to allow the attributes fname and lname to be accessed individually as well.

Examples
a1 = Name("john", "SMITH")
a1.fname ➞ "John"

a1.lname ➞ "Smith"

a1.fullname ➞ "John Smith"

a1.initials ➞ "J.S"
Notes
Make sure only the first letter of each name is capitalised.
Check the Resources tab for some helpful tutorials on Python classes.
    """


class Name(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fname(self):
        return self.first_name.capitalize()

    def lname(self):
        return self.last_name.capitalize()

    def initials(self):
        return f"{self.first_name.capitalize()[0]}"+"."+f"{self.last_name.capitalize()[0]}"


a1 = Name("john", "SMITH")
print(a1.fname())
print(a1.lname())
print(a1.initials())

"""9.Counting Instances Created from a Class
Write a Composer class that has three instance variables:

name
dob
country
Add an additional class variable .count which counts the total number of instances created.

Examples
# Just finished writing the Composer class
Composer.count ➞ 0

c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
Composer.count ➞ 1

c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
c3 = Composer("Johannes Brahms", 1833, "Germany")
Composer.count ➞ 3
Notes
N/A
    """


class Composer:
    count = 0

    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        Composer.count += 1


c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
print(Composer.count)

"""10.Book Shelf
Create a Book class that has two attributes:

.title
.author
and two methods:

A method named .get_title() that returns: "Title: " + the instance title.
A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:

Pride and Prejudice - Jane Austen (PP)
Hamlet - William Shakespeare (H)
War and Peace - Leo Tolstoy (WP)
The name of the new instances should be PP, H, and WP, respectively.

For instance, if I instantiated the following book using this Book class:

Harry Potter - J.K. Rowling (HP)
I would get the following attributes and methods:

Examples
HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Title: Harry Potter"
HP.get_author() ➞ "Author: J.K. Rowling"
Notes
Read more about Python classes in Resources.
Remember, after you've finished writing the class and its methods, you must instantiate it through the creation of new objects.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return "Title: "+f"{self.title}"

    def get_author(self):
        return "Author: "+f"{self.author}"


PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamlet", "William Shakespeare")
WP = Book("War and Peace", "Leo Tolstoy")
HP = Book("Harry Potter", " J.K. Rowling")
print(H.get_title())
print(H.get_author())
print(WP.get_author())
print(HP.get_title())

"""11.Food for Everyone!
Create a Person class which will have three properties:

Name
List of foods they like
List of foods they hate
In this class, create the method taste():

It will take in a food name as a string.
Return {person_name} eats the {food_name}.
If the food is in the person's like list, add 'and loves it!' to the end.
If it is in the person's hate list, add 'and hates it!' to the end.
If it is in neither list, simply add an exclamation mark to the end.
Examples
p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"

p1.taste("cheese") ➞ "Sam eats the cheese!"

p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"
Notes
A person can have an empty list for foods they hate and/or love.
Check the Resources for some helpful tutorials on Python classes.
    """


class Person():

    def __init__(self, name, likes, hates):
        self.name = name
        self.likes = likes
        self.hates = hates

    def taste(self, food_name):
        if food_name in self.likes:
            return f"{self.name} eats the {food_name} and loves it!"
        elif food_name in self.hates:
            return f"{self.name} eats the {food_name} and hates it!"
        else:
            return f"{self.name} eats the {food_name}!"


p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste("ice cream"))
print(p1.taste("cheese"))
print(p1.taste("carrots"))

"""12.Big Countries
A country can be said as being big if it is:

Big in terms of population.
Big in terms of area.
Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

Population is greater than 250 million.
Area is larger than 3 million square km.
Also, create a method which compares a country's population density to another country object. Return a string in the following format:

{country} has a {smaller / larger} population density than {other_country}
Examples
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"
Notes
Population density is calculated by dividing the population by the area.
Area is given in square km.
The input will be in the format (name_of_country, population, size_in_km2), where name_of_country is a string and the other two inputs are integers.
        """


class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.check_if_big()

    def check_if_big(self):
        if self.population > 250000 or self.area > 3000000:

            return True
        else:
            return False

    def compare_pd(self, other_country):
        self_density = self.population / self.area
        other_density = other_country.population / other_country.area

        if self_density > other_density:
            return f"{self.name} has a larger population density than {other_country.name}"
        elif self_density < other_density:
            return f"{self.name} has a smaller population density than {other_country.name}"
        else:
            return f"{self.name} has the same population density as {other_country.name}"


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
print(australia.is_big)
print(andorra.compare_pd(australia))
