#!/usr/bin/python3
def print_last_digit(number):
    for n in number:
        print(abs(n) % 10, end="")
        return(abs(n) % 10)
