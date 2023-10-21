import termcolor
import colorama
import os
import random

ulColor  = "red"
llColor  = "red"
sColor   = "red"
nColor   = "red"
message  = None

UL = list("QWERTYUIOPASDFGHJKLZXCVBNM")
LL = list("qwertyuiopasdfghjklzxcvbnm")
SC = list("!@#$%^&*()-_=+{}\|;:',<.>/?")
NC = list("1234567890")

passwordAsArray = []
password        = ""

colorama.init()

passwordSigns = []
os.system("cls||clear")
print(f"""
            Welcome to random password generator!
            first, you need to say what you want to be 
            included in password, write a letter according
            to legend below to say what will be included 
            in your password (upper/lower case letter doesn't matter)
            color on the legend tells you which one is currently enabled
        """)
while True:
    print(f"""
            {termcolor.colored("UL", ulColor)} - your password will include uppercase letters
            {termcolor.colored("LL", llColor)} - your password will include lowercase letters
            {termcolor.colored("S", sColor)} - your password will include special characters
            {termcolor.colored("N", nColor)} - your password will include Numbers
            Next - finish choosing what your password will include, and start setting how long it will be
          """)
    passwordIncludes = input(">")
    passwordIncludes = passwordIncludes.upper()
    match passwordIncludes:
        #im sorry for this monster, i wanted to do it in function but i couldn't edit variable in it and i don't know how to do it in other way, so i did this if else monster
        case "UL":
            if ulColor == "red":
                passwordSigns.extend(UL)
                ulColor = "green"
            else:
                passwordSigns = [i for i in passwordSigns if i not in UL]
                ulColor = "red"
        case "LL":
            if llColor == "red":
                passwordSigns.extend(LL)
                llColor = "green"
            else:
                passwordSigns = [i for i in passwordSigns if i not in LL]
                llColor = "red"
        case "S":
            if sColor == "red":
                passwordSigns.extend(SC)
                sColor = "green"
            else:
                passwordSigns = [i for i in passwordSigns if i not in SC]
                sColor = "red"
        case "N":
            if nColor == "red":
                passwordSigns.extend(NC)
                nColor = "green"
            else:
                passwordSigns = [i for i in passwordSigns if i not in NC]
                nColor = "red"
        case "NEXT":
            if(passwordSigns != []):
                break
            message = termcolor.colored("sorry you have to choose something, I need some letters to make password from","red" ,attrs=["underline"])
        case _:
            message = termcolor.colored("wrong input", "red", attrs=["underline"])
    os.system('cls||clear')
    if message != None:
        print(message)
    message = None
os.system('cls||clear')
while True:
    print("okay, now how long password you want to generate?")
    try:
        PasswordLength = int(input(">"))
        break
    except:
        termcolor.cprint("sorry, but this is not a number", "red", attrs=["underline"])
for i in range(PasswordLength):
    randomFromArray = random.choice(passwordSigns)
    passwordAsArray.append(randomFromArray)
password = password.join(passwordAsArray)
print(f"your generated password is: {password}")
input("")
        