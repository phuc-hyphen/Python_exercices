"""check password"""
import string


def check(pw):
    if len(pw) < 6 or len(pw) > 12:
        return 0
    lower = False
    upper = False
    spe = False
    for letter in pw:
        if letter.islower():
            lower = True
        if letter.isupper():
            upper = True
        if letter in "@&$#":
            spe = True
    if lower and upper and not spe:
        return 1


password = input(" enter your pass : ")
while check(password) == 0:
    print(" Password invalid \n")
    password = input("Enter your pass : ")
print(" Password invalid \n")
