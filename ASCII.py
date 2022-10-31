def table(value):
    ASCII = {
        # Альтернативная ASCII-таблица
        "А": [1, 1, 0, 1, 0, 1, 1, 1],
        "Б": [1, 0, 0, 1, 0, 1, 1, 1],
        "В": [0, 1, 0, 1, 0, 1, 1, 1]
    }
    arr = ASCII[value]

    return arr


print(table("А"))
