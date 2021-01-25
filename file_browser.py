"""Module handling file browser"""
import shutil
from tkinter import filedialog, messagebox
from ciphers import write_key, load_key, encrypt_file, decrypt_file


write_key() # everytime you run the app, a new key is generated
key = load_key()


def browse_key():
    """Load your pre-owned key"""
    try:
        f_d = filedialog.askopenfilename()
        # shutil - high level file operations library
        shutil.copyfile(f_d, "key.key")
    except FileNotFoundError:
        result = messagebox.askyesno("Cancel", "Do you want to cancel?")
        if not result:
            browse_key()


def export_key():
    """Export current key"""
    try:
        f_d = filedialog.asksaveasfilename(confirmoverwrite=True)
        shutil.copy("key.key", f_d)
    except FileNotFoundError:
        result = messagebox.askyesno("Cancel", "Do you want to cancel?")
        if not result:
            export_key()


def browse_files_to_save(text):
    """File browser for saving"""
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
    """File Browser for encryption"""
    try:
        f_d = filedialog.askopenfilename()
        encrypt_file(f_d, key)
    except FileNotFoundError:
        result = messagebox.askyesno("Cancel", "Do you want to cancel?")
        if not result:
            browse_files_to_encrypt()


def browse_files_to_decrypt():
    """File browser for decryption"""
    try:
        f_d = filedialog.askopenfilename()
        decrypt_file(f_d, key)
    except FileNotFoundError:
        result = messagebox.askyesno("Cancel", "Do you want to cancel?")
        if not result:
            browse_files_to_decrypt()
