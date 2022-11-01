from ASCII import table, alphabet

# Матрица для первичной перемешки
initialPermutationMatrix = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Матрица для расширения ключа 32-48
expandMatrix = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# Матрица перестановок для ключа
keyPermutationMatrix1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# Матрица перестановок, используемая после каждой замены SBox для каждого раунда
eachRoundPermutationMatrix = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# Матрица конкратенации
finalPermutationMatrix = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

SboxesArray = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],

    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],

    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],

    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],

    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],

    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],

    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],

    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]


def main():
    message = "АБДИЕВ Н"
    key = "БОЛОТКАН"
    print("Текст для шифровки: ", message)
    print("Ключ: ", key)

    # Шифровка
    ciphertext = DES(message, key, True)
    # Дешифровка
    text = DES(ciphertext, key, False)

    print("Зашифрованый текст: %r " % ciphertext)
    print("Дешифрованный текст: ", text)


def DES(message, key, isEncrypt):
    result = []

    # Переводим текст на двоичный вид
    if isEncrypt == True:
        block = getASCII(message)

    if isEncrypt == False:
        block = stringToBitArray(message)

    # Начальная перестановка IP
    block = permutation(block, initialPermutationMatrix)

    # Получаем значание ключа
    key = generateKey(key)

    # Разделяем блок на левый и правый подблоки по 32 бита
    leftBlock, rightBlock = nSplit(block, 32)

    # Производим раширение для правого подблока до 48 бит
    expandedRightMatrix = expand(rightBlock, expandMatrix)

    # Сложение по модулю 2 расширенного правого подблока с ключем
    temp = xor(key, expandedRightMatrix)

    # S-box
    Sbox = SboxSubstitution(temp)

    # Перестановка Р
    perm = permutation(Sbox, eachRoundPermutationMatrix)

    # XOR левого подблока с правым
    xorValue = xor(leftBlock, perm)

    # Меняем местами правый и левый подблоки
    leftBlock = rightBlock
    rightBlock = xorValue

    # Выполняем итоговую операцию перестановки
    result += permutation(rightBlock + leftBlock, finalPermutationMatrix)

    if isEncrypt == True:
        # Конвертивуем биты в текст
        finalResult = bitArrayToString(result)
    if isEncrypt == False:
        # Конвертивуем биты в текст
        finalResult = bitArrayToASCII(result)

    return finalResult


def binValue(val, bitSize):
    """Функция для возврата двоичного значения в виде строки заданного размера."""

    binVal = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]

    # Добавление с необходимым количеством нулей впереди
    while len(binVal) < bitSize:
        binVal = "0" + binVal

    return binVal


def getASCII(value):
    bitArray = []

    for i in value:
        bitArray += table(i)

    return bitArray


def nSplit(list, n):
    """Функция для разделения списка на куски размера n."""
    # Фрагментирование и возврат массива фрагментов размера n
    return [list[i: i + n] for i in range(0, len(list), n)]


def expand(array, table):
    """Функция расширения массива с помощью таблицы."""

    return [array[element - 1] for element in table]


def xor(list1, list2):
    """Функция для возврата XOR двух списков."""
    # Возврат xor двух списков
    return [element1 ^ element2 for element1, element2 in zip(list1, list2)]


def permutation(array, table):
    """Функция для перестановки массива с использованием таблицы."""
    # Возврат переставленного результата
    return [array[element - 1] for element in table]


def generateKey(array):
    """Функция генерации ключей для разных раундa DES."""

    array = getASCII(array)

    mas = []
    # Первично удаляем каждый 8 бит
    mas[:] = [x for i, x in enumerate(array, start=1) if i % 8]
    # Вторично удаляем каждый 8 бит
    mas[:] = [x for i, x in enumerate(mas, start=1) if i % 8]
    # Удаляем последний элемент списка
    del mas[47]

    return mas


def SboxSubstitution(bitArray):
    """Функция замены всех байтов с помощью Sbox."""

    # Разбиваем массив на 8 подмассивов по 6 элементов
    blocks = nSplit(bitArray, 6)
    result = []

    for i in range(len(blocks)):
        block = blocks[i]
        # Получаем значение строки
        row = int(str(block[0]) + str(block[5]), 2)
        # Получаем значение столбца
        column = int(''.join([str(x) for x in block[1:-1]]), 2)
        # Получаем значение из S-box
        sboxValue = SboxesArray[i][row][column]
        # Конвертируем целовисленное значение в битовое
        binVal = binValue(sboxValue, 4)
        # Сохраняем результат в массиве
        result += [int(bit) for bit in binVal]

    return result


def stringToBitArray(text):
    """Funtion to convert a string into a list of bits."""

    # Initializing variable required
    bitArray = []
    for letter in text:
        # Getting binary (8-bit) value of letter
        binVal = binValue(letter, 8)
        # Making list of the bits
        binValArr = [int(x) for x in list(binVal)]
        # Apending the bits to array
        bitArray += binValArr

    # Returning answer
    return bitArray


def bitArrayToString(array):
    """Функция для преобразования списка битов в строку."""

    # Разделение массива битов на 8 байтов
    byteChunks = nSplit(array, 8)
    stringBytesList = []

    # Для каждого байта
    for byte in byteChunks:
        bitsList = []
        for bit in byte:
            bitsList += str(bit)
        # Добавление байта в строковой форме к stringBytesList
        stringBytesList.append(''.join(bitsList))

    # Преобразование каждого stringByte в char (сначала преобразование в int с основанием 2), а затем объединение
    result = ''.join([chr(int(stringByte, 2)) for stringByte in stringBytesList])

    return result

def bitArrayToASCII(array):
    """Функция для преобразования списка битов в строку."""

    # Разделение массива битов на 8 байтов
    byteChunks = nSplit(array, 8)
    text = ""

    for byte in byteChunks:
        letter = alphabet(byte)
        text += letter

    return text


if __name__ == '__main__':
    main()
