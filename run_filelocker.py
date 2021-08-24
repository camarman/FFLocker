#----- File Locker for Windows OS -----#

#--- The program can encrypt these file extensions---#

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

# Note: It may encrypt other file extensions as well

# ----- Importing Modules ----- #

import os
import secrets
from string import ascii_letters
from time import sleep

from Crypto import Random
from Crypto.Cipher import AES

# ----- Generating Random Password ----- #


def generate_random_password():
    flag = True
    print('\nPlease enter the number of bytes in the password')
    print('Allowed Values:16, 24, 32')
    while flag:
        nbytes = int(input('Byte number:'))
        if nbytes in [16, 24, 32]:
            flag = False
        else:
            print('ERROR: Please enter one of the options given above')
    random_password = ''
    ascii_extended = ascii_letters + '0123456789' + r'!"#$%&()*+,-./;<>?@[\]^_`{|}~'
    for i in range(nbytes):
        random_password += secrets.choice(ascii_extended)
    return random_password

# ----- Generating User Entered Password ----- #


def generate_password():
    flag = True
    while flag:
        password = input('\nEnter a password:')
        passwordLen = len(password)
        if passwordLen in [16, 24, 32]:
            flag = False
        else:
            print(
                'ERROR: Your password have {} characters. The length of the password must be 16, 24 or 32'.format(passwordLen))
    return password

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
    encfilePATH = filePATH + '.enc'
    os.rename(filePATH, encfilePATH)
    in_file.close()


def decrypt_file(encfilePATH, key):
    with open(encfilePATH, 'rb+') as in_file:
        plaintext = in_file.read()
        dec = decrypt(plaintext, key)
    filePATH = encfilePATH[:-4]
    with open(filePATH, 'wb') as out_file:
        out_file.write(dec)
    out_file.close()

#----- Running Locker ------#


def run_filelocker_encryption():
    print('\nPlease type the path of the file')
    flagPATH = True
    while flagPATH:
        filePATH = input('PATH:')
        if filePATH[-3:] == 'enc':
            print('ERROR: Encryption cannot be applied to the files with .enc extension!')
            print('\nPlease re-enter the path')
        elif filePATH[-3:] != 'enc':
            flagPATH = False
    print('\nPlease choose the type of the encryption')
    print('------------')
    print('Type "rp" to generate random password')
    print('Type "up" to enter a password')
    print('------------')
    flag_encryption_type = True
    while flag_encryption_type:
        encryption_type = input('Encryption type:')
        if encryption_type != 'rp' and encryption_type != 'up':
            print('ERROR: Please type one of the commands given above!')
        else:
            flag_encryption_type = False
    # Generating random password
    if encryption_type == 'rp':
        password = generate_random_password()
        print('Generating random password...')
        sleep(1.5)
    elif encryption_type == 'up':
        password = generate_password()
    key = str.encode(password)
    print('\nIMPORTANT: Save this password to decrypt your file!')
    print('PASSWORD:{}\n'.format(password))
    print('Encrypting the file...')
    sleep(1.5)
    encrypt_file(filePATH, key)
    print('Encryption is successful!')


def run_filelocker_decryption():
    print('\nPlease type the path of the file')
    flagPATH = True
    while flagPATH:
        encfilePATH = input('PATH:')
        if encfilePATH[-3:] != 'enc':
            print('ERROR: Decryption can only be applied to the files with .enc extension!')
            print('\nPlease re-enter the path')
        else:
            flagPATH = False
    print('\nPlease enter the password')
    password = input('PASSWORD:')
    key = str.encode(password)
    print('\nDecrypting the file...')
    sleep(1.5)
    try:
        decrypt_file(encfilePATH, key)
        print('Decryption is successful!')
        print('\nDo you want to remove the encrypted file?')
        print('[Y]: Yes\t[N]: No')
        flag_answer = True
        while flag_answer:
            answer = input('')
            if answer != 'Y' and answer != 'N':
                print('ERROR: Please type one of the commands given above!')
            else:
                flag_answer = False
        if answer == 'Y':
            os.remove(encfilePATH)
            print('\nRemoving the encrypted file...')
            sleep(1.5)
        elif answer == 'N':
            pass
    except:
        print('\nDecryption is not successful!')
        print('Please enter the correct password')


def run_filelocker():
    print('\t--Welcome to the File Locker--\n')
    print('Do you want to encrypt or decrypt the file?')
    print('[E]: Encrypt\t[D]: Decrypt')
    flag_method = True
    while flag_method:
        answer = input('')
        if answer != 'E' and answer != 'D':
            print('ERROR: Please type one of the commands given above!')
        else:
            flag_method = False
    if answer == 'E':
        run_filelocker_encryption()
        os.system('pause')
        print('\nThis page will close in 90 seconds. Please save the password to decrypt the file!')
        sleep(90)
    elif answer == 'D':
        run_filelocker_decryption()
        os.system('pause')
        print('\nThis page will close in 10 seconds')
        sleep(10)


run_filelocker()
