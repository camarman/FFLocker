#----- Folder Locker for Windows -----#

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
    in_file.close()


def decrypt_file(filePATH, key):
    with open(filePATH, 'rb+') as in_file:
        plaintext = in_file.read()
        in_file.seek(0)
        dec = decrypt(plaintext, key)
        in_file.write(dec)
        in_file.truncate()
    in_file.close()


def get_all_filePaths(folderPATH):
    result = []
    for dirpath, dirnames, filenames in os.walk(folderPATH):
        result.extend([os.path.join(dirpath, filename)
                      for filename in filenames])
    return result

# ----- Encrypting/Decrypting every file inside a folder ----- #

def encrypt_folder(folderPATH, key):
    for filePATH in get_all_filePaths(folderPATH):
        encrypt_file(filePATH, key)


def decrypt_folder(folderPATH, key):
    for filePATH in get_all_filePaths(folderPATH):
        decrypt_file(filePATH, key)

#----- User Inputs -----#

# If you want to generate a random key enter this information
nbytes = 16  # The num of bytes can be 16, 24, or 32 (128, 192, 256 bits)

# if you want to generate personalized key, enter a message
message = 'Always Wishing You Were?'

# Generated key via user input
key = generate_user_entered_key(message)

# The path of the folder that you want to encrypt
folderPATH = r'C:\Users\Arman\Desktop\TestFolder'

#----- Running Locker ------#

encrypt_folder(folderPATH, key)

# decrypt_folder(folderPATH, key)
