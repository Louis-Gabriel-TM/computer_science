"""
The question
============
Write a program that prints the numbers fom 1 to 100.
But for multiples of 3 print 'Fizz' instead of the number and for multiples of 5 print 'Buzz'. For numbers which are multiples of both 3 and 5 print 'FizzBuzz'.
"""


def naive_fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)


def alternative_fizzbuzz():
    for n in range(1, 101):
        fizz = (n % 3 == 0)
        buzz = (n % 5 == 0)

        if fizz and buzz:
            print("FizzBuzz")
        elif fizz:
            print("Fizz")
        elif buzz:
            print("Buzz")
        else:
            print(n)


def short_fizzbuzz():
    for n in range(1, 101):
        print("Fizz" * (not n % 3) + "Buzz" * (not n % 5) or n)


if __name__ == "__main__":
    pass
