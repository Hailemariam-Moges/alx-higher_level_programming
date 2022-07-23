#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Haile", "Abie")
say_my_name("Alex", "Abie")
say_my_name("Habtu")
try:
    say_my_name(15, "Abie")
except Exception as e:
    print(e)
