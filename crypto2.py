# Табличный шифр 

table = {
    'т': 'о', 'у': 'ъ', 'ф': 'и', 'х': 'ф', 'ц': 'э', 'ч': 'у',
    'ш': 'л', 'щ': 'з', 'ъ': 'ж', 'ы': 'в', 'ь': 'г', 'э': 'с',
    'ю': 'ю', 'я': 'п', 'а': 'т', 'б': 'ч', 'в': 'н', 'г': 'к',
    'д': 'ё', 'е': 'я', 'ё': 'м', 'ж': 'щ', 'з': 'ш', 'и': 'б',
    'й': 'х', 'к': 'ь', 'л': 'а', 'м': 'ц', 'н': 'ы', 'о': 'е',
    'п': 'й', 'р': 'р', 'с': 'д'
}

def table_cipher(text):
    result = ""
    for ch in text:
        if ch.lower() in table:
            new_ch = table[ch.lower()]
            if ch.isupper():
                new_ch = new_ch.upper()
            result += new_ch
        else:
            result += ch
    return result



text = input("Введите текст для табличного шифра: ")
print("Результат:", table_cipher(text))
