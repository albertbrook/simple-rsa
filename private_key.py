def private_key():
    try:
        with open("id_rsa.txt") as file:
            rsa = file.read()[1:-1].split(", ")
    except FileNotFoundError:
        print("Private key not found, please confirm")
    else:
        try:
            with open("secret.txt") as file:
                secret_num = file.read()[1:-1].split(", ")
        except FileNotFoundError:
            print("encrypted text not found, please confirm")
        else:
            string = ""
            for secret_char in secret_num:
                string += chr(int(secret_char) ** int(rsa[0]) % int(rsa[1]))
            print(string)


if __name__ == '__main__':
    private_key()
