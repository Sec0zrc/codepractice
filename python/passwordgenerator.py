#!/usr/bin/python
import random
import sys


def print_help():
    print("Usage: Pyton passwordgenerator.py [\'passwordlength\']", end=" ")


# generate password function
# password must contain number \uppercase letter  \lowercase letter \special symbols
# range(48,58)  0-9
# range(65,91) A-Z
# range(97,123) a-z
# range(33,65) special symbols and number
def generate_password(length):
    password = []
    count = 0
    while count != length:
        match count % 4:
            case 0:
                password.append(chr(random.randint(48, 58)))
                count += 1
                pass
            case 1:
                password.append(chr(random.randint(65, 91)))
                count += 1
                pass
            case 2:
                password.append(chr(random.randint(97, 123)))
                count += 1
                pass
            case 3:
                password.append(chr(random.randint(33, 65)))
                count += 1

    str = ''
    for i in password:
        str += i
    return str


if __name__ == '__main__':
    passwordlen = 18

    try:
        passwordlen = int(sys.argv[1])
        if (passwordlen > 12 and passwordlen < 30):
            password = generate_password(passwordlen)
            print("password:{}".format(password))
        else:
            print("Password Length must be positive and more than 12 and less than 30")
    except ValueError:
        print("Please enter a number!", end=" ")
    except IndexError:
        print_help()
