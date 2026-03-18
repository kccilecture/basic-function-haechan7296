def add(a, b):
    add = a + b
    return add

def sub(a, b):
    sub = a - b
    return sub

def mul(a, b):
    mul = a * b
    return mul


def div(a, b):
    div = a / b
    return div


def power(base, pow):
    power = base ** pow
    return power


def square(base):
    square = base ** 2
    return square


def greet(이름="낯선자", 나이=20):
    if 나이 >= 20 and 나이 <= 40:
        return f"안녕하신가 {이름}!"
    elif 나이 > 40:
        return f"안녕하십니까 {이름}!"
    else: 
        return f"안녕 {이름}!"