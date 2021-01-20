"""Moduł w którym znajdują się funkcje obsługujące okno dialogowe"""
import shutil
from tkinter import filedialog
from ciphers import write_key, load_key, encrypt_file, decrypt_file

# Generowanie klucza do szyfrowania plików
write_key() # Przy każdym włączeniu aplikacji generuje się nowy klucz
key = load_key()


def browse_key():
    """
    Funkcja pozwalająca na wgranie własnego klucza
    """
    f_d = filedialog.askopenfilename()
    # shutil - biblioteka obslugująca operacje high-level na plikach
    shutil.copyfile(f_d, "key.key")


def browse_files_to_save(text):
    """Funkcja obsługujące okno dialogowe do zapisu"""
    # asksaveasfile zwraca 'None' jeśli wybrana zostanie opcja cancel w file browser
    f_d = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if f_d is None:
        return
    text_to_save = str(text)
    f_d.write(text_to_save)
    f_d.close()


def browse_files_to_encrypt():
    """Funkcja obsługująca okno dialogowe do szyfrowania pliku"""
    f_d = filedialog.askopenfilename()
    encrypt_file(f_d, key)
    if f_d is None:
        return


def browse_files_to_decrypt():
    """Funkcja obsługująca okno dialogowe do odszyfrowania pliku"""
    f_d = filedialog.askopenfilename()
    decrypt_file(f_d, key)
    if f_d is None:
        return
