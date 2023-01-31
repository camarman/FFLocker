# ========== Folder Locker for GNU/LINUX ==========

# ========= Importing Modules ==========

import os
import secrets
import shutil
import sys
from pathlib import Path
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
    ascii_extended = ascii_letters + '0123456789' + \
        r'!"#$%&()*+,-./;<>?@[\]^_`{|}~'
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


def decrypt_file(encfolderPATH, encfilePATH, key):
    with open(encfilePATH, 'rb+') as in_file:
        plaintext = in_file.read()
        dec = decrypt(plaintext, key)
    with open(encfolderPATH[:-3] + encfilePATH[len(encfolderPATH):-4], 'wb') as out_file:
        out_file.write(dec)
    out_file.close()


def get_all_filePaths(folderPATH):
    result = []
    for dirpath, dirnames, filenames in os.walk(folderPATH):
        result.extend([os.path.join(dirpath, filename) for filename in filenames])
    return result


def get_all_folderPATHS(folderPATH):
    folderPATHS = []
    for dirpath, dirnames, filenames in os.walk(folderPATH):
        folderPATHS.append(dirpath)
    return folderPATHS


def mkdir_folder(folderPATHS):
    mainfolderPATH = folderPATHS[0][:-3]
    p = Path(mainfolderPATH)
    p.mkdir(parents=True, exist_ok=True)
    for folderPATH in folderPATHS[1:]:
        folderPATH = mainfolderPATH + folderPATH[len(mainfolderPATH)+3:]
        p = Path(folderPATH)
        p.mkdir(parents=True, exist_ok=True)


# ========== Encrypting/Decrypting every file inside a folder ==========

def encrypt_folder(folderPATH, key):
    for filePATH in get_all_filePaths(folderPATH):
        encrypt_file(filePATH, key)
    encfolderPATH = folderPATH + 'ENC'
    os.rename(folderPATH, encfolderPATH)


def decrypt_folder(encfolderPATH, key):
    for encfilePATH in get_all_filePaths(encfolderPATH):
        decrypt_file(encfolderPATH, encfilePATH, key)


# ========== Running Locker ==========

def run_folderlocker_encryption():
    print('\nPlease type the path of the folder')
    flagPATH = True
    while flagPATH:
        folderPATH = input('PATH:')
        if folderPATH[-3:] == 'ENC':
            print('ERROR: Encryption cannot be applied to the folders with ENC extension!')
            print('\nPlease re-enter the path')
        elif folderPATH[-3:] != 'ENC':
            flagPATH = False
    print('\nPlease choose the type of the encryption')
    print('-'*10)
    print('Type "rp" to generate random password')
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
    print('\nIMPORTANT: Save this password to decrypt your folder!')
    print('PASSWORD:{}\n'.format(password))
    print('Encrypting the folder...')
    encrypt_folder(folderPATH, key)
    for _ in range(30):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        sleep(0.1)
        sys.stdout.write('\b')
    print('Encryption is successful!')


def run_folderlocker_decryption():
    print('\nPlease type the path of the folder')
    flagPATH = True
    while flagPATH:
        encfolderPATH = input('PATH:')
        if encfolderPATH[-3:] != 'ENC':
            print(
                'ERROR: Decryption can only be applied to the folders with ENC extension!')
            print('\nPlease re-enter the path')
        else:
            flagPATH = False
    print('\nPlease enter the password')
    password = input('PASSWORD:')
    key = str.encode(password)
    print('\nDecrypting the folder...')
    for _ in range(20):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        sleep(0.1)
        sys.stdout.write('\b')
    mkdir_folder(get_all_folderPATHS(encfolderPATH))
    try:
        decrypt_folder(encfolderPATH, key)
        print('Decryption is successful!')
        print('\nDo you want to remove the encrypted folder?')
        print('[y]: yes\t[n]: no')
        flag_answer = True
        while flag_answer:
            answer = input('')
            if answer != 'y' and answer != 'n':
                print('ERROR: Please type one of the commands given above!')
            else:
                flag_answer = False
        if answer == 'y':
            shutil.rmtree(encfolderPATH, ignore_errors=True)
            print('\nRemoving the encrypted folder...')
            for _ in range(20):
                sys.stdout.write(next(spinner))
                sys.stdout.flush()
                sleep(0.1)
                sys.stdout.write('\b')
            print('Encrypted folder has been removed')
        elif answer == 'n':
            pass
    except:
        print('\nDecryption is not successful!')
        print('Please enter the correct password')
        # since the decryption is not successful, when can delete the created folder
        shutil.rmtree(encfolderPATH[:-3], ignore_errors=True)


def run_folderlocker():
    print('Starting Folder Locker...')
    for _ in range(15):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        sleep(0.1)
        sys.stdout.write('\b')
    print('Do you want to encrypt or decrypt the folder?')
    print('[e]: encrypt\t[d]: decrypt')
    flag_method = True
    while flag_method:
        answer = input('')
        if answer != 'e' and answer != 'd':
            print('ERROR: Please type one of the commands given above!')
        else:
            flag_method = False
    if answer == 'e':
        run_folderlocker_encryption()
    elif answer == 'd':
        run_folderlocker_decryption()

run_folderlocker()
