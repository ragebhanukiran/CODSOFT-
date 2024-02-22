import string
import random
def password_generator():
    letters = string.ascii_letters
    digits = string.digits
    sp = string.punctuation

    password = ""
    npass = int(input("choose length of the password : "))
    if npass < 0:
        print("length of password must be a positive integer!")
    nletters = int(input("choose number of alphabets required in your password : "))
    if nletters <= npass :
        for i in range(nletters):
            password += random.choice(letters)
        if npass == nletters :
            print("Password Generated :",password)
        elif nletters < npass:
            ndigits = int(input("choose number of digits required in your password : "))
            if npass >= len(password):
                for i in range(ndigits):
                    password += random.choice(digits)
                if npass == len(password):
                    password = "".join(random.sample(password,len(password)))
                    print("Password Generated :",password)
                elif npass > len(password):
                    nsp = int(input("choose number of special characters required in your password : "))
                    for i in range(nsp):
                        password += random.choice(sp)
                        password = "".join(random.sample(password,len(password)))
                    print("Password Generated :",password)
                if npass > len(password):
                    print("size of the password is less than required length !!")
            else :
                    print("size of the password exceeded !!")
        else :
                print("size of the password exceeded !!")
    else :
                    print("size of the password exceeded !!")
password_generator()










