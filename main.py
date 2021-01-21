"""
Autor - Mateusz Śliwa grupa gc03 - mateusz.sliwa1@edu.uekat.pl
AppJar - GUI https://github.com/jarvisteach/appJar
TkInter - Okno dialogowe https://docs.python.org/3/library/tk.html
Cryptography - szyfrowanie plików https://pypi.org/project/cryptography/
"""
from appJar import gui
import ciphers
import file_browser

app = gui("CryptoApp", useTtk=True)
app.setSize(600, 600)
app.showSplash("CryptoApp", fill='#07244f', stripe='black', fg='white', font=44)


def press(button):
    """
    Metoda obsługująca przyciski
    Obecnie otwarta zakładka (tab) będzie "decydować" o tym, która funkcja zostanie wywołana
    """
    tab = app.getTabbedFrameSelectedTab("CryptoApp")
    result = app.getTextArea("OutputArea")

    if button == "Encrypt" and tab == "Caesar cipher":
        caesar_text = app.getTextArea("caesar_text")
        caesar_key = app.getSpinBox("caesar_key")
        app.clearAllTextAreas()
        app.setTextArea("OutputArea", ciphers.caesar_cipher(caesar_text, caesar_key))

    elif button == "Decrypt" and tab == "Caesar cipher":
        caesar_text = app.getTextArea("caesar_text")
        caesar_key = app.getSpinBox("caesar_key")
        ciphers.caesar_decipher(caesar_text, caesar_key)
        app.clearAllTextAreas()
        app.setTextArea("OutputArea", ciphers.caesar_decipher(caesar_text, caesar_key))

    elif button == "Encrypt" and tab == "XOR cipher":
        xor_text = app.getTextArea("xor_text")
        xor_key = app.getEntry("xor_key")
        app.clearAllTextAreas()
        app.setTextArea("OutputArea", ciphers.xor_cipher(xor_text, xor_key))

    elif button == "Decrypt" and tab == "XOR cipher":
        xor_text = app.getTextArea("xor_text")
        xor_key = app.getEntry("xor_key")
        app.clearAllTextAreas()
        app.setTextArea("OutputArea", ciphers.xor_cipher(xor_text, xor_key))

    elif button == "Encrypt" and tab == "ROT13 cipher":
        rot13_text = app.getTextArea("rot13_text")
        app.clearAllTextAreas()
        app.setTextArea("OutputArea", ciphers.rot13_cipher(rot13_text))

    elif button == "Decrypt" and tab == "ROT13 cipher":
        rot13_text = app.getTextArea("rot13_text")
        app.clearAllTextAreas()
        app.setTextArea("OutputArea", ciphers.rot13_decipher(rot13_text))

    elif button == "Encrypt" or button == "Decrypt" and tab == "AtBash cipher":
        atbash_text = app.getTextArea("atbash_text")
        app.clearAllTextAreas()
        app.setTextArea("OutputArea", ciphers.atbash_cipher(atbash_text))

    elif button == "Save":
        file_browser.browse_files_to_save(result)

    elif button == "Encrypt a file":
        file_browser.browse_files_to_encrypt()

    elif button == "Decrypt a file":
        file_browser.browse_files_to_decrypt()
    elif button == "Generate key":
        ciphers.write_key()
    elif button == "Load a key":
        file_browser.browse_key()
    elif button == "Export key":
        file_browser.export_key()


def error_popup(message):
    app.infoBox("Error", message)


app.startTabbedFrame("CryptoApp", row=0, column=0)
# Zakładka - Szyfr Cezara
app.startTab("Caesar cipher")
app.addLabel("l1", "Caesar's cipher encryption", row=0, column=0)
app.addTextArea("caesar_text", text="Message to cipher/decipher")
app.addSpinBoxRange("caesar_key", 0, 25)
app.setSpinBoxPos("caesar_key", 0, callFunction=True)
app.stopTab()

# Zakładka - Szyfr XOR
app.startTab("XOR cipher")
app.addLabel("l2", "XOR cipher encryption")
app.addTextArea("xor_text", text="Message to cipher/decipher")
app.addEntry("xor_key")
app.setEntryDefault("xor_key", "Key (a character <A;Z>)")
app.stopTab()

# Zakładka - Szyfr ROT13
app.startTab("ROT13 cipher")
app.addLabel("l3", "ROT13 cipher encryption")
app.addTextArea("rot13_text", text="Message to cipher/decipher")
app.stopTab()

# Zakładka - Szyfr AtBash
app.startTab("AtBash cipher")
app.addLabel("l4", "AtBash cipher encryption")
app.addTextArea("atbash_text", text="Message to cipher or decipher")
app.stopTab()
app.stopNotebook()

# Separatory + przyciski
app.addButtons(["Encrypt", "Decrypt"], press)
app.addButton("Save", press)
app.addLabel("Result:")
app.addTextArea("OutputArea")
app.addHorizontalSeparator()
app.addButtons(["Generate key", "Export key", "Load a key"], press)
app.addButtons(["Encrypt a file", "Decrypt a file"], press)
app.go()
