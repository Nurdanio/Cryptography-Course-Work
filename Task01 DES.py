from Functions import binValue, getASCII, nSplit, expand, xor, permutation, stringToBitArray, bitArrayToString, \
    bitArrayToASCII, initialPermutationMatrix, SboxesArray, expandMatrix, eachRoundPermutationMatrix, finalPermutationMatrix


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
    block = []

    # Переводим текст на двоичный вид
    if isEncrypt:
        block = getASCII(message)

    if not isEncrypt:
        block = stringToBitArray(message)

    # Начальная перестановка IP
    block = permutation(block, initialPermutationMatrix)

    # Получаем значение ключа
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

    final = ""
    if isEncrypt:
        # Конвертивуем биты в текст
        final = bitArrayToString(result)
    if not isEncrypt:
        # Конвертивуем биты в текст
        final = bitArrayToASCII(result)

    return final


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

if __name__ == '__main__':
    main()
