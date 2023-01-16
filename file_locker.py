# ========== File Locker for GNU/LINUX ==========

# ========== Importing Modules ==========

import os
import secrets
import sys
from string import ascii_letters
from time import sleep

from Crypto import Random
from Crypto.Cipher import AES

# ========== Spinning Cursor Animation ==========

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()

# ========== Generating Random Password ==========

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


# ========== Generating User Entered Password ==========

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


# ========== Main Functions ==========

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


# ========== Running Locker ==========

def run_filelocker_encryption():
    print('\nPlease enter the path of the file')
    flagPATH = True
    while flagPATH:
        filePATH = input('PATH:')
        if filePATH[-3:] == 'enc':
            print('ERROR: Encryption cannot be applied to the files with .enc extension!')
            print('\nPlease re-enter the path')
        elif filePATH[-3:] != 'enc':
            flagPATH = False
    print('\nPlease choose the type of the encryption')
    print('-'*10)
    print('Type "rp" to a generate random password')
    print('Type "up" to enter a password')
    print('-'*10)
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
        for _ in range(20):
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            sleep(0.1)
            sys.stdout.write('\b')
    elif encryption_type == 'up':
        password = generate_password()
    key = str.encode(password)
    print('\nIMPORTANT: Save this password to decrypt your file!')
    print('PASSWORD:{}\n'.format(password))
    print('Encrypting the file...')
    encrypt_file(filePATH, key)
    for _ in range(30):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        sleep(0.1)
        sys.stdout.write('\b')
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
    for _ in range(20):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        sleep(0.1)
        sys.stdout.write('\b')
    try:
        decrypt_file(encfilePATH, key)
        print('Decryption is successful!')
        print('\nDo you want to remove the encrypted file?')
        print('[y]: yes\t[n]: no')
        flag_answer = True
        while flag_answer:
            answer = input('')
            if answer != 'y' and answer != 'n':
                print('ERROR: Please type one of the commands given above!')
            else:
                flag_answer = False
        if answer == 'y':
            os.remove(encfilePATH)
            print('\nRemoving the encrypted file...')
            for _ in range(20):
                sys.stdout.write(next(spinner))
                sys.stdout.flush()
                sleep(0.1)
                sys.stdout.write('\b')
            print('Encrypted file has been removed')
        elif answer == 'n':
            pass
    except:
        print('\nDecryption is not successful!')
        print('Please enter the correct password')


def run_filelocker():
    print('Starting File Locker...')
    for _ in range(15):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        sleep(0.1)
        sys.stdout.write('\b')
    print('Do you want to encrypt or decrypt the file?')
    print('[e]: encrypt\t[d]: decrypt')
    flag_method = True
    while flag_method:
        answer = input('')
        if answer != 'e' and answer != 'd':
            print('ERROR: Please type one of the commands given above!')
        else:
            flag_method = False
    if answer == 'e':
        run_filelocker_encryption()
    elif answer == 'd':
        run_filelocker_decryption()

run_filelocker()
