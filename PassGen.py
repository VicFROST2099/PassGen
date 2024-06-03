import secrets          # for randomisation of characters
import string           # for calling specific charcaters
import os               # clearing terminal 
os.system("clear")      # for linux terminal
os.system("cls")        # for windows terminal

print("\t\t\t\t***All passwords generated will contain lowercase letters***")
while True:
    try:
        lengthPass = int(input("Please enter the length of characters for your password. (eg: 9, min: 6): "))
        if lengthPass <= 0:
            print("Please enter a valid number")
        elif lengthPass >= 6:
            break
    except ValueError:
        print("Invalid value entered, please enter an integer")

while True:
    try:
        upperChars = input("Please select if you want uppercase characters included, yes or no?: ")
        if upperChars not in ["yes","no"]:
            raise ValueError("Please enter a valid option")
        else:
            break
    except ValueError as e:
        print(f"An error occured, {e}")

while True:
    try:
        numbers = input("Please select if you want numbers included, yes or no?: ")
        if numbers not in ["yes","no"]:
            raise ValueError("Please enter a valid option")
        else:
            break
    except ValueError as g:
        print(f"An error occured, {g}")

while True:
    try:
        specialChars = input("Please select if you want special characters included, yes or no?: ")
        if specialChars not in ["yes","no"]:
            raise ValueError("Please enter a valid option")
        else:
            break
    except ValueError as f:
        print(f"An error occured, {f}") 

def genPassword(length, upper, nums, spChars):
    # Option 1 - just letters (lowercase)
    if length > 5 and upper == "no" and nums == "no" and spChars == "no":
        chars = string.ascii_lowercase
        password = ""
        for i in range(length):
            rndmstring = "".join(secrets.choice(chars))
            password = password + rndmstring
        return password

    # Option 2 - just letters (lower and upper case)
    elif length > 5 and upper == "yes" and nums == "no" and spChars == "no":
        chars = string.ascii_lowercase + string.ascii_uppercase
        while True:
            password = ""
            con_lower = False
            con_upper = False
            for i in range(length):
                rndmstring = "".join(secrets.choice(chars))
                password = password + rndmstring
            for char in password:
                if char in string.ascii_lowercase:
                    con_lower = True
                if char in string.ascii_uppercase:
                    con_upper = True
            if con_lower and con_upper:
                break
            else:
                continue
        return password

    # Option 3 - letters and numbers 
    elif length > 5 and upper == "yes" and nums == "yes" and spChars == "no":
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        while True:
            password = ""
            con_lower = False
            con_upper = False
            con_dig = False
            for i in range(length):
                rndmstring = "".join(secrets.choice(chars))
                password = password + rndmstring
            for char in password:
                if char in string.ascii_lowercase:
                    con_lower = True
                if char in string.ascii_uppercase:
                    con_upper = True
                if char in string.digits:
                    con_dig = True
            if con_lower and con_upper and con_dig:
                break
            else:
                continue
        return password

    # Option 4 - letters, numbers and special characters
    elif length > 5 and upper == "yes" and nums == "yes" and spChars == "yes":
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        while True:
            password = ""
            con_lower = False
            con_upper = False
            con_dig = False
            con_spec = False
            for i in range(length):
                rndmchar = "".join(secrets.choice(chars))
                password = password + rndmchar
            for char in password:
                if char in string.ascii_lowercase:
                    con_lower = True
                if char in string.ascii_uppercase:
                    con_upper = True
                if char in string.digits:
                    con_dig = True
                if char in string.punctuation:
                    con_spec = True
            if con_lower and con_upper and con_dig and con_spec:
                break
            else:
                continue
        return password
        
    # Option 5 - letters (lower, no upper), numbers and no special characters
    elif length > 5 and upper == "no" and nums == "yes" and spChars == "no":
        chars = string.ascii_lowercase + string.digits
        while True:
            password = ""
            con_lower = False
            con_dig = False
            for i in range(length):
                rndmstring = "".join(secrets.choice(chars))
                password = password + rndmstring
            for char in password:
                if char in string.ascii_lowercase:
                    con_lower = True
                if char in string.digits:
                    con_dig = True
            if con_lower and con_dig:
                break
            else:
                continue
        return password

    # Option 6 - letters (lower, no upper), numbers and special characters
    elif length > 5 and upper == "no" and nums == "yes" and spChars == "yes":
        chars = string.ascii_lowercase + string.digits + string.punctuation
        while True:
            password = ""
            con_lower = False
            con_dig = False
            con_spec = False
            for i in range(length):
                rndmstring = "".join(secrets.choice(chars))
                password = password + rndmstring
            for char in password:
                if char in string.ascii_lowercase:
                    con_lower = True
                if char in string.digits:
                    con_dig = True
                if char in string.punctuation:
                    con_spec = True
            if con_lower and con_dig and con_spec:
                break
            else:
                continue
        return password

    # Option 7 - letters (lower, no upper), special characters and no numbers
    elif length > 5 and upper == "no" and nums == "no" and spChars == "yes":
        chars = string.ascii_lowercase + string.punctuation
        while True:
            password = ""
            con_lower = False
            con_spec = False
            for i in range(length):
                rndmstring = "".join(secrets.choice(chars))
                password = password + rndmstring
            for char in password:
                if char in string.ascii_lowercase:
                    con_lower = True
                if char in string.punctuation:
                    con_spec = True
            if con_lower and con_spec:
                break
            else:
                continue
        return password   

    # Option 8 - letters (lower + upper), special and no numbers
    elif length > 5 and upper == "yes" and nums == "no" and spChars == "yes":
        chars = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
        while True:
            password = ""
            con_lower = False
            con_upper = False
            con_spec = False
            for i in range(length):
                rndmstring = "".join(secrets.choice(chars))
                password = password + rndmstring
            for char in password:
                if char in string.ascii_lowercase:
                    con_lower = True
                if char in string.ascii_uppercase:
                    con_upper = True
                if char in string.punctuation:
                    con_spec = True
            if con_lower and con_upper and con_spec:
                break
            else:
                continue
        return password
     
password = genPassword(lengthPass, upperChars, numbers, specialChars)
print(f"The generated password is:\n{password}")






