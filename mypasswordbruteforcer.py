"""
Author: Christopher Duncan
Build Date: 01/21/2022
This project is brute force password cracker.

This was a very fun project and gave me more insight brute forcing a password with Python.

I made sure to not copy any code to fully understand the project from top to bottom. Any of the mandatory methods
will in fact still be the same.

The videos I used for reference are below:
https://www.youtube.com/watch?v=M9OPVXtnBu8

1. We start off with installing the pyautogui module for the graphic user interface. I haven't tried this with tkinter
but I'm very sure it would work as well. (pip install pyautogui)
2. Going to import the random and pyautogui modules
3. Store all possible character and numbers in the chars variable
4. Covert the string brute_chars to a list
5. Get password from user using pyautogui interface
6. Declare the guessed password to store a gui password as en empty string.
7. Using a while loop, so essentially we will continuously loop as long as the guessed_password is not the exact pass.
8. Give the guessed_password random chars from the chars_list with the len of the user_password. Ex: the user_password
is "abc" so the random length will be 3 characters.
9. Using random.choices(list, k) function. k: represents how much random characters we want from a list.
10. Display the guessed characters
11. Here if guessed_password is the password then print the password thus breaking the loop.
12. Run it. It should work!
13. If you want all possible characters besides the ones we've put in the brute list then uncomment the info below.
(We will use the (import string module and printable)
"""

import random
import pyautogui
import string

# brute_chars = string.printable
brute_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
chars_list = list(brute_chars)

user_password = pyautogui.password("Please Enter Your Password: ")

guessed_password = ""


while guessed_password != user_password:
    guessed_password = random.choices(chars_list, k=len(user_password))

    print("<====================" + str(guessed_password)  + "<=======================") # 10

    if guessed_password == list(user_password): # 11
        print("Your password is : " + "".join(guessed_password))
        break



