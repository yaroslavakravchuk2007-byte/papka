# Шифр Цезаря 

class Caesar:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, key):
        self.key = key
        self._encode = {}
        self._decode = {}
        # Создаём таблицы для кодирования и декодирования
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            enc = self.alphabet[(i + key) % len(self.alphabet)]
            dec = self.alphabet[(i - key) % len(self.alphabet)]
            self._encode[letter] = enc
            self._encode[letter.upper()] = enc.upper()
            self._decode[enc] = letter
            self._decode[enc.upper()] = letter.upper()

    def encode(self, text):
        return ''.join([self._encode.get(ch, ch) for ch in text])

    def decode(self, text):
        return ''.join([self._decode.get(ch, ch) for ch in text])



key = int(input("Введите сдвиг : "))
cipher = Caesar(key)

text = input("Введите текст: ")
encoded = cipher.encode(text)
decoded = cipher.decode(encoded)

print("Зашифровано:", encoded)
print("Расшифровано:", decoded)
