# ГОСТ 28147-89
def main():
    # Исходные данные
    text = "ABDIEV N"
    key = "ALINa posla sobiratb gribysdfsfd"

    # Шифровка
    ciphertext = GOST(text, key)

    # Дешифровка
    plaintext = GOST(ciphertext, key)

    # Вывод результатов
    print("Исходное сообщение:", text)
    print("Ключ: ", key)
    print("Зашифрованый текст:", ciphertext)
    print("Дешифрованный текст:", plaintext)


def GOST(text, key):
    """Основная функция алгоритма ГОСТ"""

    # Переводим текст в битовый массивый
    block = stringToBitArray(text)

    # Разбиваем на правый и на левый блок
    leftBlock, rightBlock = nSplit(block, 32)

    # Присваеваем значения правого блока в левый блок следующей итерации
    leftBlock1 = rightBlock

    # Переводим ключ в битовый массив и разбиваем ключ на подключи
    keys = stringToBitArray(key)
    K1 = gettingKeys(keys)

    # Суммируем по модулю 32
    xorBlock = xor32(rightBlock, K1)
    # Шаг замены S-box
    SResult = SBlocks(xorBlock)
    # Делаем сдвиг на 11 элементов
    ShiftResult = Shift(SResult, 11)
    # Делаем операцию xor между правым и левым блоками
    rightBlock1= xor(ShiftResult, leftBlock)
    # Полный битовый массив
    encrypt = leftBlock1 + rightBlock1

    finalResult = bitArrayToString(encrypt)

    # print("Левый блок: ", len(leftBlock), leftBlock)
    # print("Правый блок:", len(rightBlock), rightBlock)
    # print("Подключ: ", len(K1), K1)
    # print("S-box массив:", len(SResult), SResult)
    # print("После сдвига:", len(ShiftResult), ShiftResult)
    # print("Блок R1:",len(rightBlock1), rightBlock1)
    # print("Итог:", len(encrypt), encrypt)
    # print(finalResult)

    return finalResult

def nSplit(list, n):
    """ Метод для разделения массива на части"""

    return [list[i: i + n] for i in range(0, len(list), n)]

def xor32(list1, list2):
    """Надо с этой хуйней поебаться"""

    # result = []
    # for i, j in zip(list1, list2):
    #     m = (i + j) % 32
    #     result.append(m)
    # return result

    return [element1 ^ element2 for element1, element2 in zip(list1, list2)]

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

    return list[n:]+list[:n]

def binToInt(block):
    """Функция перевода двоичного значения в десятичное"""

    number = 0
    len_dat = len(block)
    for i in range(0, len_dat):
        number += int(block[i]) * (2**(len_dat - i - 1))

    return number

def BinValue(val, bitSize):
    """Функция получения битового значания"""

    binVal = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]

    while len(binVal) < bitSize:
        binVal = "0" + binVal

    return binVal

def stringToBitArray(text):
    """Функция перевода в массив битов"""

    bitArray = []
    for letter in text:
        # Getting binary (8-bit) value of letter
        binVal = BinValue(letter, 8)
        # Making list of the bits
        binValArr = [int(x) for x in list(binVal)]
        # Apending the bits to array
        bitArray += binValArr

    return bitArray

def bitArrayToString(array):
    """Функция для преобразования списка битов в строку"""

    # Разделение массива битов на 8 байтов
    byteChunks = nSplit(array, 8)
    # Инициализируем переменные
    stringBytesList = []
    stringResult = ''
    # Проходим для каждому байту
    for byte in byteChunks:
        bitsList = []
        for bit in byte:
            bitsList += str(bit)
        # Добавление байта в виде строки в stringBytesList
        stringBytesList.append(''.join(bitsList))

    # Преобразование каждого stringByte в char (сначала преобразование в int с основанием 2)
    # а затем объединение
    result = ''.join([chr(int(stringByte, 2)) for stringByte in stringBytesList])

    # Возвращаемый результат
    return result

def xor(list1, list2):
    """Фунция сложения по модулю 2"""

    return [element1 ^ element2 for element1, element2 in zip(list1, list2)]

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