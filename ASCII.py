# Альтернативная ASCII-таблица
ASCII = {
    " ": [0, 0, 0, 1, 0, 0, 0, 0],
    "А": [1, 1, 0, 0, 0, 0, 0, 0],
    "Б": [1, 1, 0, 0, 0, 0, 0, 1],
    "В": [1, 1, 0, 0, 0, 0, 1, 0],
    "Г": [1, 1, 0, 0, 0, 0, 1, 1],
    "Д": [1, 1, 0, 0, 0, 1, 0, 0],
    "Е": [1, 1, 0, 0, 0, 1, 0, 1],
    "Ж": [1, 1, 0, 0, 0, 1, 1, 0],
    "З": [1, 1, 0, 0, 0, 1, 1, 1],
    "И": [1, 1, 0, 0, 1, 0, 0, 0],
    "Й": [1, 1, 0, 0, 1, 0, 0, 1],
    "К": [1, 1, 0, 0, 1, 0, 1, 0],
    "Л": [1, 1, 0, 0, 1, 0, 1, 1],
    "М": [1, 1, 0, 0, 1, 1, 0, 0],
    "Н": [1, 1, 0, 0, 1, 1, 0, 1],
    "О": [1, 1, 0, 0, 1, 1, 1, 0],
    "П": [1, 1, 0, 0, 1, 1, 1, 1],
    "Р": [1, 1, 0, 1, 0, 0, 0, 0],
    "С": [1, 1, 0, 1, 0, 0, 0, 1],
    "Т": [1, 1, 0, 1, 0, 0, 1, 0],
    "У": [1, 1, 0, 1, 0, 0, 1, 1],
    "Ф": [1, 1, 0, 1, 0, 1, 0, 0],
    "Х": [1, 1, 0, 1, 0, 1, 0, 1],
    "Ц": [1, 1, 0, 1, 0, 1, 1, 0],
    "Ч": [1, 1, 0, 1, 0, 1, 1, 1],
    "Ш": [1, 1, 0, 1, 1, 0, 0, 0],
    "Щ": [1, 1, 0, 1, 1, 0, 0, 1],
    "Ъ": [1, 1, 0, 1, 1, 0, 1, 0],
    "Ы": [1, 1, 0, 1, 1, 0, 1, 1],
    "Ь": [1, 1, 0, 1, 1, 1, 0, 0],
    "Э": [1, 1, 0, 1, 1, 1, 0, 1],
    "Ю": [1, 1, 0, 1, 1, 1, 1, 0],
    "Я": [1, 1, 0, 1, 1, 1, 1, 1]
}


def table(value): return ASCII[value]


def alphabet(array):
    for k, v in ASCII.items():
        if v == array:
            return k


