import math,random

def random_auth():
    digits = "0123456789"
    auth = ""
    for i in range(6):
        auth += random.choice(digits)
    return auth

if __name__ == "__main__":
    print("6 digits otp: ",random_auth())
