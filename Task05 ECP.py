from Task03_RSA import keyGenerate
from Task04_Hash import HashFunction


def main():

    # 'А', 'Б', 'Д', 'И', 'Е', 'В'
    message = [1, 2, 5, 10, 6, 3]

    # Постоянные для ЭЦП RSA (Вариант №1)
    p = 17
    q = 11

    # Хеш-образ
    m = HashFunction(p, q, message)

    # Значения открытого и закрытого ключей
    publicKey, privateKey = keyGenerate(p, q)

    # Проводим шифровку хеш-образа
    S = EDS(m, privateKey)

    # Проводим дешифровку хеш-образа
    M = EDS(S, publicKey)

    print("Xеш-образ:", m)
    print("Зашифрованный хеш-образ:", S)
    print("Дешифрованный хеш-образ:", M)
    if m == M:
        print("Хеш-образы совпадают!")
    else:
        print("Хеш-образы не совпадают!")


def EDS(a, key):
    """Функция вычисления цифровой подписи"""
    z, n = key
    x = (a ** z) % n
    return x


if __name__ == '__main__':
    main()





