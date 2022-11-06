# ГОСТ 28147-89
from ASCII import table, alphabet
from Functions import binValue, getASCII, nSplit, xor, stringToBitArray, bitArrayToString, bitArrayToASCII


def main():
    """Основная функция алгоритма ГОСТ 28147-89"""

    # Исходные данные
    message = "АБДИЕВ Н"
    key = "РЕНТГЕНОЭЛЕКТРОКАРДИОГРАФИЧЕСКИЙ"

    print("Текст для шифровки: ", message)
    print("Ключ: ", key)

    # Шифровка
    ciphertext = GOST(message, key, True)
    print("Зашифрованый текст: %r " % ciphertext)

    # Дешифровка
    text = GOST(ciphertext, key, False)
    print("Дешифрованный текст: ", text)


def GOST(text, key, isEncrypt):
    """Основная функция алгоритма ГОСТ"""

    # Переводим ключ в битовый массив и разбиваем ключ на подключи
    keys = getASCII(key)

    # Инициализируем массивы для хранения значений текста и ключа раунда в битовом формате
    block = []
    K1 = []
    finalResult = ""

    # Условие для шифровки
    if isEncrypt:
        # Переводим текст в битовый массивый
        block = getASCII(text)
        # Генерируем ключ раунда
        K1 = gettingKeys(keys)
        # Разбиваем на правый и на левый блок
        leftBlock, rightBlock = nSplit(block, 32)

    # Условие для дешифровки
    if not isEncrypt:
        # Переводим текст в битовый массивый
        block = stringToBitArray(text)
        # Генерируем ключ раунда
        K1 = gettingKeys(keys)
        # Разбиваем на правый и на левый блок
        rightBlock, leftBlock = nSplit(block, 32)


    # Присваеваем значения правого блока в левый блок следующей итерации
    leftBlock1 = rightBlock

    # Суммируем по модулю 32
    xorBlock = mod32(rightBlock, K1)
    # Шаг замены S-box
    SResult = SBlocks(xorBlock)

    # Делаем сдвиг на 11 элементов
    ShiftResult = Shift(SResult, 11)

    # Делаем операцию xor между правым и левым блоками
    rightBlock1 = xor(ShiftResult, leftBlock)

    if isEncrypt:
        # Полный битовый массив
        encrypt = leftBlock1 + rightBlock1
        finalResult = bitArrayToString(encrypt)

    if not isEncrypt:
        encrypt = rightBlock1 + leftBlock1
        finalResult = bitArrayToASCII(encrypt)

    return finalResult


def mod32(num1, num2):
    """Функция суммирования по модулю 32"""

    # перевернуть числа для удобства выполнения операций
    num1 = num1[::-1]
    num2 = num2[::-1]

    # дополнить числа нулями
    size = max(len(num1), len(num2))

    num1 += [0] * (size - len(num1))
    num2 += [0] * (size - len(num2))

    # сложить 2 числа
    overflow = 0
    res = []
    for obj in zip(num1, num2):
        value = obj[0] + obj[1] + overflow
        overflow = value // 2
        res.append(value % 2)

    # если флаг переполнения установлен - добавить бит в начало нового числа
    if overflow == 1:
        res.append(1)

    # перевернуть число назад
    res = res[::-1]

    return res[1:]


# S-блок, используемый в алгоритме ГОСТ
SboxesArray = [
    [1, 13, 4, 6, 7, 5, 14, 4],
    [15, 11, 11, 12, 13, 8, 11, 10],
    [13, 4, 10, 7, 10, 1, 4, 9],
    [0, 1, 0, 1, 1, 13, 12, 2],
    [5, 3, 7, 5, 0, 10, 6, 13],
    [7, 15, 2, 15, 8, 3, 13, 8],
    [10, 5, 1, 13, 9, 4, 15, 0],
    [3, 9, 13, 8, 15, 2, 10, 14],
    [9, 0, 3, 4, 14, 14, 2, 6],
    [2, 10, 6, 10, 4, 15, 3, 11],
    [3, 14, 8, 9, 6, 12, 8, 1],
    [14, 7, 5, 14, 12, 7, 1, 12],
    [6, 6, 9, 0, 11, 6, 0, 7],
    [11, 8, 12, 3, 2, 0, 7, 15],
    [8, 2, 15, 11, 5, 9, 5, 5],
    [12, 12, 14, 2, 3, 11, 9, 3]
]


def SBlocks(list):
    """Функция замены всех битов с помощью Sbox"""

    # Разделяем на 8 блоков по 4 бита
    blocks = nSplit(list, 4)
    result = []
    index = 7

    # Цикл S-box, для получения необходимых значений
    for i in range(len(blocks)):
        block = blocks[i]
        # Номер строки, который нужно получить из первого и последнего бита
        column = binToInt(block)
        # Получаем значение из S-блока
        SboxValue = SboxesArray[column][index]
        # Переводим значение в битовый формат
        binVal = BinValue(SboxValue, 4)
        # Записываем в массив битовые значения
        result += [int(bit) for bit in binVal]
        # С каждым разом уменьшаем индекс на единицу
        index -= 1

    return result


def Shift(list, n):
    """Фунция для сдвига элементов на 11 позиций"""

    return list[n:] + list[:n]


def binToInt(block):
    """Функция перевода двоичного значения в десятичное"""

    number = 0
    len_dat = len(block)
    for i in range(0, len_dat):
        number += int(block[i]) * (2 ** (len_dat - i - 1))

    return number


def BinValue(val, bitSize):
    """Функция получения битового значания"""

    binVal = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]

    while len(binVal) < bitSize:
        binVal = "0" + binVal

    return binVal


def gettingKeys(key):
    """Функция для получения первых 32 бит ключа"""

    # Цикл перебора 32-х бит
    keys = []
    temp = 0
    for i in key:
        temp += 1
        if temp < 33:
            keys.append(i)
        else:
            break

    return keys


if __name__ == '__main__':
    main()