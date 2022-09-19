# Division of PEMaCS
# CSCI-121 Elements of Computer Programming II
# Recitation 1 - Encryption with a password
# *******************************************************

import string

alphabet = string.printable
ordinal_value = {ch: i for i, ch in enumerate(alphabet)}


def encrypt(message, password):
    encrypted_message = ''
    for index, ch in enumerate(message):
        pass_ch = password[index % len(password)]
        key = ordinal_value[pass_ch]
        ord_ch = ordinal_value[ch]
        shifted_ord_ch = (ord_ch + key) % len(alphabet)
        encrypted_ch = alphabet[shifted_ord_ch]
        encrypted_message += encrypted_ch
    return encrypted_message



def decrypt(message, password):
    decrypted_message = ''
    for index, ch in enumerate(message):
        pass_ch = password[index % len(password)]
        key = ordinal_value[pass_ch]
        ord_ch = ordinal_value[ch]
        shifted_ord_ch = (ord_ch - key) % len(alphabet)
        decrypted_ch = alphabet[shifted_ord_ch]
        decrypted_message += decrypted_ch
    return decrypted_message

print(encrypt("This is a test, hello world!", "Mypass"))
print(decrypt(encrypt("This is a test, hello world!", "Mypass"),"Mypass"))