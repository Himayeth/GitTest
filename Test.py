import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def check(email):
    if(re.search(regex,email)):
        print("Valid Email")

    else:
        print ("Invalid email")


if __name__ == '__main__':
    email ="ankitrai@gmail.com"
    check(email)

    email = "ankitrai"
    check(email)
