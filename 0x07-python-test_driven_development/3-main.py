#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
try:
    say_my_name("", "White")
except Exception as e:
    print(e)
try:
    say_my_name("Pete", 12)
except Exception as e:
    print(e)
try:
    say_my_name("Pete", ["Wu"])
except Exception as e:
    print(e)
