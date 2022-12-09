#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) != 113 & chr(letter) != 101:
        print("{}".format(chr(letter)), end="")
