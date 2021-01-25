"""
Cipher's logic  https://github.com/VoxelPixel/CiphersInPython
File encryption https://pypi.org/project/cryptography/
"""
from cryptography.fernet import Fernet


def caesar_cipher(text, key):
    """
    Caesar's cipher
    """
    result = ""
    # entry in appJar returns float, therefore it's got to be converted to int
    c_key = int(key)
    for i, _ in enumerate(text):
        if ord(text[i]) == 32:  # ord returns Unicode of a character (32 to is space)
            result += chr(ord(text[i]))  # chr converts int (ASCII) to char
        elif ord(text[i]) + c_key > 122:
            # after 'z' return to 'a', 'a' = 97, 'z' = 122
            template = (ord(text[i]) + c_key) - 122
            result += chr(96 + template)
        elif ord(text[i]) + c_key > 90 and ord(text[i]) <= 96:
            # return to do 'A' after 'Z'
            template = (ord(text[i]) + c_key) - 90
            result += chr(64 + template)
        else:
            # in case of letters between a-z and A-Z
            result += chr(ord(text[i]) + c_key)
    print(result)
    return result


def caesar_decipher(text, key):
    """Caesar's cipher analogic"""
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
    """XOR Cipher"""
    length = len(text)
    for i in range(length):
        text = (text[:i] +
                chr(ord(text[i]) ^ ord(key)) +
                text[i + 1:])
        print(text[i], end="")
    print("\n")
    return text


def rot13_cipher(text):
    """ROT 13 Cipher"""
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
    """Key is removed instead of added"""
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
    """AtBash cipher"""
    text = text.upper()
    alfabet = dict(A='Z', B='Y', C='X', D='W', E='V', F='U',
                  G='T', H='S', I='R', J='Q', K='P', L='O',
                  M='N', N='M', O='L', P='K', Q='J', R='I',
                  S='H', T='G', U='F', V='E', W='D', X='C',
                  Y='B', Z='A')
    result = ''
    for letter in text:
        # check for spaces
        if letter != ' ':
            # add a relevant letter from dictionary
            result += alfabet[letter]
        else:
            # add space
            result += ' '
    print("Encrypted message: {}".format(result))
    return result


# Szyfrowanie plików
def write_key():
    """Generate a key"""
    key = Fernet.generate_key()  # Generate key and save it
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """Load a key to the current catalogue"""
    return open("key.key", "rb").read()


def encrypt_file(filename, key):
    """File encryption"""
    f_key = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f_key.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(filename, key):
    """File decryption"""
    f_key = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f_key.decrypt(encrypted_data)
    decrypted_data.decode("utf-8")  # decode bytes to string
    with open(filename, "wb") as file:
        file.write(decrypted_data)
