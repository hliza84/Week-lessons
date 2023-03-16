"""3.Write a function that takes an integer minutes and converts it to seconds.
"""
minit=int(1.3)
seconds=minit*60
print(seconds)

"""1.For this challenge, you are supposed to find the sum of the digits of a two-digit number.
"""   
n=11
sum=0
sum=int(n//10)+int(n%10)
print(sum)

"""2. A repdigit is a positive number composed out of the same digit. Create a function that takes an two-digit integer and returns whether it's a repdigit or not.
"""
n=44
x=int(n/10)==int(n%10)
print(x)

"""4.Create a function that takes the age in years and returns the age in days.
"""
years=0
age=int(years)
days=age*365
print(days)

"""6.Create a function that accepts a measurement value in inches and returns the equivalent of the measurement value in feet.
"""
inches=100
feet=inches/12
print(feet)

"""7.Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.
"""
x=15
if x%2==0:
    print("even")
else:
    print("odd")

""" 5.Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
"""
hours=1.3
minutes = hours * 60;
seconds = minutes * 60;
print(seconds);


def time_to_seconds(hours, minutes):
    """
    This function takes two integers hours and minutes as input, converts them to seconds, and adds them
    """
    return hours * 3600 + minutes * 60
print(time_to_seconds(1, 18)) # Output: 5400





