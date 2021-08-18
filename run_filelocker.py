#----- File Locker for Windows -----#

#--- It works for ---#

# .jpg
# .txt
# .pdf
# .xlsx
# .ppt/pptx
# .docx
# .png
# .py
# .wav
# .m4a

# Note: It may also work for other types of file

# ----- Importing Modules ----- #

import os
import secrets

from Crypto import Random
from Crypto.Cipher import AES

# ----- Generating Random Keys ----- #

def generate_key(nbytes):
    return secrets.token_bytes(nbytes)


def generate_printible_hex_key(nbytes):
    key_bytes = str.encode(secrets.token_hex(nbytes))
    return key_bytes


def generate_printible_key(nbytes):
    key_bytes = str.encode(secrets.token_urlsafe(nbytes))
    return key_bytes

# ----- Generating User Entered Key ----- #

def generate_user_entered_key(message):
    avaliable_nbytes = [16, 24, 32]
    messageLen = len(message)
    if messageLen in avaliable_nbytes:
        key_bytes = str.encode(message)
        return key_bytes
    else:
        raise ValueError(
            'Your message has {} characters. The length of the message must be 16, 24 or 32'.format(messageLen))

# ----- Main Functions ----- #

def pad(s):
    padding_size = AES.block_size - len(s) % AES.block_size
    return s + b"\0" * padding_size, padding_size


def encrypt(message, key):
    message, padding_size = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_bytes = iv + cipher.encrypt(message) + bytes([padding_size])
    return enc_bytes


def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:-1])
    padding_size = ciphertext[-1] * (-1)
    return plaintext[:padding_size]


def encrypt_file(filePATH, key):
    with open(filePATH, 'rb+') as in_file:
        plaintext = in_file.read()
        in_file.seek(0)
        enc = encrypt(plaintext, key)
        in_file.write(enc)
        in_file.truncate()
    encfilePATH = filePATH + 'enc'
    os.rename(filePATH, encfilePATH)
    in_file.close()


def decrypt_file(encfilePATH, key):
    with open(encfilePATH, 'rb+') as in_file:
        plaintext = in_file.read()
        dec = decrypt(plaintext, key)
    filePATH = encfilePATH[:-3]
    with open(filePATH, 'wb') as out_file:
        out_file.write(dec)
    out_file.close()

#----- User Inputs -----#

# If you want to generate a random key enter this information
nbytes = 16  # The num of bytes can be 16, 24, or 32 (128, 192, 256 bits)

# if you want to generate personalized key, enter a message
message = 'no clear mind...'

# Generated key via user input
key = generate_user_entered_key(message)

# The path of the folder that you want to encrypt
filePATH = r'C:\Users\Arman\Desktop\TestFolder\test.jpg'

# The path of the folder that you want to decrypt
encfilePATH = r'C:\Users\Arman\Desktop\TestFolder\test.jpgenc'

#----- Running Locker ------#

def run_filelocker_encryption(filePATH, key):
    if filePATH[-3:] == 'enc':
        raise TypeError('The encryption cannot be performed on .enc files')
    elif filePATH[-3:] != 'enc':
        encrypt_file(filePATH, key)


def run_filelocker_decryption(encfilePATH, key):
    if encfilePATH[-3:] != 'enc':
        raise TypeError('The decryption cannot be performed on non .enc files')
    else:
        decrypt_file(encfilePATH, key)

#TODO: Fix the error problems, Improve the user interface with commends

# run_filelocker_encryption(filePATH, key)

run_filelocker_decryption(encfilePATH, key)