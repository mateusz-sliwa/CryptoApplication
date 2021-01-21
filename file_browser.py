"""Moduł w którym znajdują się funkcje obsługujące okno dialogowe"""
import shutil
from tkinter import filedialog, messagebox
from ciphers import write_key, load_key, encrypt_file, decrypt_file

# Generowanie klucza do szyfrowania plików
write_key() # Przy każdym włączeniu aplikacji generuje się nowy klucz
key = load_key()


def browse_key():
    """Wczytaj własny klucz """
    try:
        f_d = filedialog.askopenfilename()
        # shutil - biblioteka obslugująca operacje high-level na plikach
        shutil.copyfile(f_d, "key.key")
    except FileNotFoundError:
        result = messagebox.askyesno("Cancel", "Do you want to cancel?")
        # w przypadku gdy wybrana zostanie opcja "No" po "Cancel" powtórz wykonanie funkcji
        if not result:
            browse_key()


def export_key():
    """ Eksportuj klucz """
    try:
        f_d = filedialog.asksaveasfilename(confirmoverwrite=True)
        shutil.copy("key.key", f_d)
    except FileNotFoundError:
        result = messagebox.askyesno("Cancel", "Do you want to cancel?")
        if not result:
            export_key()


def browse_files_to_save(text):
    """Funkcja obsługujące okno dialogowe do zapisu"""
    if not text:
        messagebox.showwarning("Error", "Result field is empty!")
    else:
        try:
            f_d = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
            text_to_save = str(text)
            f_d.write(text_to_save)
            f_d.close()
        except AttributeError:
            result = messagebox.askyesno("Cancel", "Do you want to cancel?")
            if not result:
                browse_files_to_save(text)


def browse_files_to_encrypt():
    """Funkcja obsługująca okno dialogowe do szyfrowania pliku"""
    try:
        f_d = filedialog.askopenfilename()
        encrypt_file(f_d, key)
    except FileNotFoundError:
        result = messagebox.askyesno("Cancel", "Do you want to cancel?")
        if not result:
            browse_files_to_encrypt()


def browse_files_to_decrypt():
    """Funkcja obsługująca okno dialogowe do odszyfrowania pliku"""
    try:
        f_d = filedialog.askopenfilename()
        decrypt_file(f_d, key)
    except FileNotFoundError:
        result = messagebox.askyesno("Cancel", "Do you want to cancel?")
        if not result:
            browse_files_to_decrypt()
