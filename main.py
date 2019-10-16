from create_rsa import create_rsa
from public_key import public_key
from private_key import private_key


def welcome():
    print("*" * 50)
    print("Welcome, all translators rely on Baidu Fanyi\n"
          "\n"
          "1.Create rsa\n"
          "2.Encrypted text\n"
          "3.Declassified text\n"
          "4.Display help\n"
          "\n"
          "0.Exit system")
    print("*" * 50)


if __name__ == '__main__':
    welcome()
    while True:
        x = input("Please select operation function: ")
        if x == "1":
            create_rsa()
        elif x == "2":
            public_key()
        elif x == "3":
            private_key()
        elif x == "4":
            welcome()
        elif x == "0":
            break
        else:
            print("Invalid instruction")
