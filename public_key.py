def public_key():
    try:
        with open("id_rsa_pub.txt") as file:
            rsa = file.read()[1:-1].split(", ")
    except FileNotFoundError:
        print("Public key not found, please confirm")
    else:
        string = input("string = ")
        secret_num = []
        for char in string:
            secret_char = ord(char) ** int(rsa[0]) % int(rsa[1])
            secret_num.append(secret_char)
        with open("secret.txt", "w") as file:
            file.write(str(secret_num))


if __name__ == '__main__':
    public_key()
