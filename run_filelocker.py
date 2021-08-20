#----- File Locker for Windows OS -----#

#--- The program can encrypt these file types---#

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

# Note: It may encrypt other file types as well

# ----- Importing Modules ----- #

import os
import secrets
from time import sleep

from Crypto import Random
from Crypto.Cipher import AES

# ----- Generating Random Key ----- #


def generate_key(nbytes):
    return secrets.token_bytes(nbytes)

# ----- Generating User Entered Key ----- #


def generate_user_entered_key():
    avaliable_nbytes = [16, 24, 32]
    flag = True
    while flag:
        key = input('\nEnter a Key:')
        keyLen = len(key)
        if keyLen in avaliable_nbytes:
            flag = False
        else:
            print(
                'Error: Your key has {} characters. The length of the key must be 16, 24 or 32'.format(keyLen))
    key_bytes = str.encode(key)
    return key_bytes

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
        filePATH = r'{}'.format(input(''))
        if filePATH[-3:] == 'enc':
            print('Error: The encryption cannot be performed on the .enc files!')
            print('\nPlease re-enter the path')
        elif filePATH[-3:] != 'enc':
            flagPATH = False
    print('\nPlease choose an encryption option')
    print('------------')
    print('Type "rk" to generate random key')
    print('Type "uk" to create key yourself')
    print('------------')
    flag_key_type = True
    while flag_key_type:
        key_type = input('Key Type:')
        if key_type != 'uk' and key_type != 'rk':
            print('Error: Please type one of the commands given above!\n')
        else:
            flag_key_type = False
    # Generated key via user input
    if key_type == 'uk':
        key = generate_user_entered_key()
        print('\nIMPORTANT: Save this key to decrypt your files in the future!')
        print('KEY:{}\n'.format(key.decode('utf-8')))
        print('Encrypting the file...')
        sleep(1.5)
        encrypt_file(filePATH, key)
        print('Encryption is successful!')
    # Generating random keys
    elif key_type == 'rk':
        nbytes = 0
        while nbytes not in [16, 24, 32]:
            print('\nPlease enter the number of bytes in the key - (16, 24, 32)')
            nbytes = int(input('Byte num:'))
            if nbytes in [16, 24, 32]:
                print('Generating random key...\n')
                sleep(1.5)
                key = generate_key(nbytes)
                print(
                    '\nIMPORTANT: Save this key to decrypt your file in the future!')
                print('KEY:{}\n'.format(key.hex()))
                print('Encrypting the file...')
                sleep(1.5)
                encrypt_file(filePATH, key)
                print('Encryption is successful!')


def run_filelocker_decryption():
    print('\nPlease type the path of the file')
    flagPATH = True
    while flagPATH:
        encfilePATH = r'{}'.format(input(''))
        if encfilePATH[-3:] != 'enc':
            print('Error: The decryption cannot be performed on the non .enc files')
            print('\nPlease re-enter the path')
        else:
            flagPATH = False
    print('\nPlease enter the key to decrypt the file')
    key = input('Key:')
    try:
        # if the key is generated from random bytes
        key = bytes.fromhex(key)
    except:
        # if the key is generated by the user input
        key = str.encode(key)
    print('\nDecrypting the file...')
    sleep(1.5)
    try:
        decrypt_file(encfilePATH, key)
        print('\nDecryption is successful!')
        print('\nDo you want to remove the encrypted file? y/n')
        flag_answer = True
        while flag_answer:
            answer = input('')
            if answer != 'y' and answer != 'n':
                print('Error: Please type one of the commands given above!\n')
            else:
                flag_answer = False
        if answer == 'y':
            os.remove(encfilePATH)
            print('\nRemoving the encrypted file...')
            sleep(1.5)
        elif answer == 'n':
            pass
    except:
        print('\nDecryption is not successful!')
        print('Please enter a correct key')


def run_filelocker():
    print('--Welcome to the File Locker--\n')
    print('Do you want to encrypt(e) or decrypt(d) the file?  e/d')
    flag_method = True
    while flag_method:
        answer = input('')
        if answer != 'e' and answer != 'd':
            print('Error: Please type one of the commands given above!\n')
        else:
            flag_method = False
    if answer == 'e':
        run_filelocker_encryption()
        os.system('pause')
        print('\nThis page will close in 90 seconds. Please save the key to decrypt files in the future!')
        sleep(90)
    elif answer == 'd':
        run_filelocker_decryption()
        os.system('pause')
        print('\nThis page will close in 10 seconds')
        sleep(10)


run_filelocker()
