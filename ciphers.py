"""
Logika cyfrów https://github.com/VoxelPixel/CiphersInPython
Szyfrowanie plików https://pypi.org/project/cryptography/
Fernet gwarantuje, że zaszyfrowana za jego pomocą wiadomość nie może zostać dczytana bez klucza.
"""
from cryptography.fernet import Fernet


def caesar_cipher(text, key):
    """
    Szyfr Cezara:
    Każda litera tekstu jawnego (niezaszyfrowanego) zastępowana jest inną
    oddaloną od niej o stałą liczbę pozycji w alfabecie
    """
    result = ""
    # entry w appJar zwracają tylko zmienne typu float zatem należy je przekonwertować jawnie na int
    c_key = int(key)
    for i, _ in enumerate(text):
        if ord(text[i]) == 32:  # ord zwraca Unicode znaku (32 to spacja)
            result += chr(ord(text[i]))  # chr konwertuje int (ASCII) do zmienneij typu char
        elif ord(text[i]) + c_key > 122:
            # po 'z' wróć do 'a', 'a' = 97, 'z' = 122
            template = (ord(text[i]) + c_key) - 122
            result += chr(96 + template)
        elif ord(text[i]) + c_key > 90 and ord(text[i]) <= 96:
            # powrót do 'A' po 'Z'
            template = (ord(text[i]) + c_key) - 90
            result += chr(64 + template)
        else:
            # warunek w przypadku występowania liter pomiędzy a-z i A-Z
            result += chr(ord(text[i]) + c_key)
    print(result)
    return result


def caesar_decipher(text, key):
    """Odwrócenie szyfru Cezara"""
    result = ""
    c_key = int(key)
    for i, _ in enumerate(text):
        if ord(text[i]) == 32:
            result += chr(ord(text[i]))
        elif ((ord(text[i]) - c_key) < 97) and ((ord(text[i]) - c_key) > 90):
            #  Oddziel klucz i dodaj 26 do bieżącej wartości znaku
            template = (ord(text[i]) - c_key) + 26
            result += chr(template)
        elif (ord(text[i]) - c_key) < 65:
            template = (ord(text[i]) - c_key) + 26
            result += chr(template)
        else:
            result += chr(ord(text[i]) - c_key)
    print("Decrypted message: ", result)
    return result


def xor_cipher(text, key):
    """Szyfr XOR"""
    length = len(text)
    for i in range(length):
        text = (text[:i] +
                chr(ord(text[i]) ^ ord(key)) +
                text[i + 1:])
        print(text[i], end="")
    print("\n")
    return text


def rot13_cipher(text):
    """Szyfr ROT13"""
    text = text.upper()
    key = 13
    result = ""
    for i, _ in enumerate(text):
        template = ord(text[i]) + key
        if ord(text[i]) == 32:
            result += " "
        elif template > 90:
            template -= 26
            result += chr(template)
        else:
            result += chr(template)
    print("Encrypted message: {}".format(result))
    return result


def rot13_decipher(text):
    """Klucz zostaje odjęty zamiast dodany"""
    text = text.upper()
    key = 13
    result = ""
    for i, _ in enumerate(text):
        template = ord(text[i]) - key
        if ord(text[i]) == 32:
            result += " "
        elif template < 65:
            template += 26
            result += chr(template)
        else:
            result += chr(template)
    print("Decrypted Message: {}".format(result))
    return result


def atbash_cipher(text):
    """Szyfr AtBash"""
    text = text.upper()
    alfabet = dict(A='Z', B='Y', C='X', D='W', E='V', F='U',
                  G='T', H='S', I='R', J='Q', K='P', L='O',
                  M='N', N='M', O='L', P='K', Q='J', R='I',
                  S='H', T='G', U='F', V='E', W='D', X='C',
                  Y='B', Z='A')
    result = ''
    for letter in text:
        # sprawdź spację
        if letter != ' ':
            # dodaj odpowiadającą literę z alfabetu
            result += alfabet[letter]
        else:
            # Dodaj spację
            result += ' '
    print("Encrypted message: {}".format(result))
    return result


# Szyfrowanie plików
def write_key():
    """Generowanie klucza do kolejnych metod"""
    key = Fernet.generate_key()  # Generuje klucz i zapisuje go do  pliku
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """Załadowanie klucza do bieżącego katalogu"""
    return open("key.key", "rb").read()


def encrypt_file(filename, key):
    """Szyfrowanie pliku"""
    f_key = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f_key.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(filename, key):
    """Odszyfrowanie pliku"""
    f_key = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f_key.decrypt(encrypted_data)
    decrypted_data.decode("utf-8")  # dekodowanie z bytes na string
    with open(filename, "wb") as file:
        file.write(decrypted_data)
