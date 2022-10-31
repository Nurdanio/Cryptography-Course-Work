from ASCII import table

key = "БОЛОТКАН"


def binValue(val, bitSize):
    """Функция для возврата двоичного значения в виде строки заданного размера."""

    binVal = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]

    # Добавление с необходимым количеством нулей впереди
    while len(binVal) < bitSize:
        binVal = "0" + binVal

    return binVal


def stringToBitArray(text):
    """Функция преобразования строки в список битов."""

    bitArray = []

    for letter in text:
        # Получение двоичного (8-битного) значения буквы
        binVal = binValue(letter, 8)
        # Составление списка бит
        binValArr = [int(x) for x in list(binVal)]
        # Добавление битов в массив
        bitArray += binValArr

    return bitArray


def keygen(array):
    mas = []
    mas[:] = [x for i, x in enumerate(array, start=1) if i % 8]
    mas[:] = [x for i, x in enumerate(mas, start=1) if i % 8]
    del mas[47]
    return mas


def getASCII(key):
    bitArray = []

    for i in key:
        bitArray += table(i)

    return bitArray

arr = getASCII(key)
print(len(arr), arr)
