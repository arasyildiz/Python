import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Şifre uzunluğunu girin: "))
print("Oluşturulan Şifre:", generate_password(length))
