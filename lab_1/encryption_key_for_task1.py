def create_polybius_square():
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    polybel_square = [
        ['а', 'б', 'в', 'г', 'д', 'е'],
        ['ж', 'з', 'и', 'й', 'к', 'л'],
        ['м', 'н', 'о', 'п', 'р', 'с'],
        ['т', 'у', 'ф', 'х', 'ц', 'ч'],
        ['ш', 'щ', 'ъ', 'ы', 'ь', 'э'],
        ['ю', 'я', 'ё', ' ', ' ', ' ']
    ]
    return polybel_square

def get_index(polybel_square, char):
    char = char.lower()
    for i in range(6):
        for j in range(6):
            if polybel_square[i][j] == char:
                return i, j