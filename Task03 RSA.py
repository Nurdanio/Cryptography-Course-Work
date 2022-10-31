p = 13
q = 19
d = 25
e = 121

# Modulus
n = p * q

# Eyler funtion
phi = (p - 1) * (q - 1)


# Encryption
def encryption(message):
    x = []
    for i in message:
        a = ord(i)
        b = (a ** e) % n
        x.append(b)
    return x


# Decryption
def decryption(crypt_message):
    y = ""
    for i in crypt_message:
        x = (int(i) ** d) % n + 988
        c = chr(x)
        y += c
    return y


message = "АНБ"
crypt_message = encryption(message)
decrypt_message = decryption(crypt_message)
print("Исходное сообщение: ", message)
print("Зашифрованное сообщение: ", crypt_message)
print("Дешифрованное сообщение: ", decrypt_message)
