import random
import string
#welcome user
print()
print("************************************GENERATE PASSWORD ********************************************")
print()
print("WELCOME TO DEFAULT PASSWORD GENERATOR")
print()
print("this app is use to grnerate\nrandom password")
print()
#pass_len = int()
# stating the code
#pass_len = input("enter your password length : ")
def stating(pass_len):
    while True:
        try:
            pass_len = int(pass_len)
            break
        except ValueError:
            print("invalid password length")
            stating()
        if(pass_len <= 0):
            print("try greater digits")
            stating()
if "__main__" == __name__:
    pass_len = input("enter your password length : ")
    stating(pass_len="dfg")
    # while True:
    #     try:
    #         pass_len = int(input("enter your password length : "))
    #     except ValueError:
    #         print("invalid password length")
    #         break
    #     if(pass_len <= 0):
    #         print("try greater digits")
#handle password lengh error
# try:
#     pass_len = int(input("enter your password length : "))
# except ValueError:
#     print("invalid password length")
#     exit()
# if(pass_len <= 0):
#     print("try greater digits")
#     exit()

# Take data from user requirement to generate password
user_digits = input("can you want to contain digits in your password YES / NO:\n")
user_lowercase_charaters = input("can you want to contain lowercase characters in your password  YES / NO:\n")
user_uppercase_charaters = input("can you want to contain uppercase characters in your password  YES / NO:\n")
user_symbols= input("can you want to contain symbols characters in your password  YES / NO:\n")

#make user requirement  in uppercase
user_digits = user_digits.upper()
user_lowercase_charaters = user_lowercase_charaters.upper()
user_uppercase_charaters = user_uppercase_charaters.upper()
user_symbols = user_symbols.upper()

# Check user for data
char = ''

#for digits
if(user_digits == "YES"):
    char += string.digits
elif(user_digits == "NO"):
    char += ""
else:
    print(f"invalid characters {user_digits}")

#for lowercase characters
if(user_lowercase_charaters == "YES"):
    char += string.ascii_lowercase
elif(user_lowercase_charaters == "NO"):
    char += ""
else:
    print(f"invalid characters {user_lowercase_charaters}")

#for uppercase characters
if(user_uppercase_charaters == "YES"):
    char += string.ascii_uppercase
elif(user_uppercase_charaters == "NO"):
    char += ""
else:
    print(f"invalid characters {user_uppercase_charaters}")

#for punctuation
if(user_symbols == "YES"):
    char += string.punctuation
elif(user_symbols == "NO"):
    char += ""
else:
    print(f"invalid characters {user_symbols}")

# Generate password
password = ""
i= 1
while i<=pass_len:
    password += random.choice(char)
    i += 1
print(f"your password is \n {password}")



# stating the code
if "__main__" == __name__:
    while True:
        try:
            pass_len = int(input("enter your password length : "))
        except ValueError:
            print("invalid password length")
        if(pass_len <= 0):
            print("try greater digits")
            
