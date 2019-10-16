from random import randint


def create_rsa():
    p = get_prime_number("p")
    q = get_prime_number("q")
    if p == q:
        print("p and q cannot be equal")
        return create_rsa()
    n = p * q
    f = (p - 1) * (q - 1)
    e = get_public_key(f)
    d = 1
    while d * e % f != 1:
        d += 1
    with open("id_rsa_pub.txt", "w") as file:
        file.write("[%s, %s]" % (e, n))
    with open("id_rsa.txt", "w") as file:
        file.write("[%s, %s]" % (d, n))


def get_prime_number(name):
    try:
        num = int(input("%s = " % name))
    except ValueError:
        print("Please enter integer")
        return get_prime_number(name)
    else:
        if num > 1 and is_prime_number(num):
            return num
        else:
            print("Please enter prime number")
            return get_prime_number(name)


def is_prime_number(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


def get_public_key(f):
    try:
        e = int(input("e = "))
    except ValueError:
        value = input("Value Wrong, Do you want random?(y or n)")
        return check_public_key(value, f)
    else:
        if e > 1 and greatest_common_divisor(e, f) == 1:
            return e
        else:
            print("Please enter the number of coprime with %d" % f)
            value = input("Do you want random?(y or n)")
            return check_public_key(value, f)


def check_public_key(value, f):
    if value == "y":
        e = random_public_key(f)
        print("e = %d" % e)
        return e
    else:
        return get_public_key(f)


def random_public_key(f):
    e = randint(2, f - 1)
    return e if greatest_common_divisor(e, f) == 1 else random_public_key(f)


def greatest_common_divisor(n1, n2):
    return n1 if n2 == 0 else greatest_common_divisor(n2, n1 % n2)


if __name__ == '__main__':
    create_rsa()
