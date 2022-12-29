# FFLocker

Locking files/folders in GNU/Linux and Windows. **The most important part of the algorithm is that during the locking process, your password is never saved on the computer and only displayed in the terminal for you to save it.**

## Installation

Clone the repository via

    git clone https://github.com/seVenVo1d/FFLocker.git

To install the required packages type:

    python3 -m pip install -r requirements.txt

In some GNU/Linux distributions, the required packages are already available, so there's no need to install any packages other than `pycryptodome`.

## Description

FFLocker uses AES encryption. You can either create a password with 16, 24, and 32 characters (which corresponds to 128, 192, 256 bits, respectively) or generate a random password with the help of the `secrets.choice`.

After you lock the file/folder, the program will change the binary data of the file/folder, and it will overwrite the files. To read/open the encrypted files, you have to enter the password.

I have programmed the code so that when you decrypt the file/folder, a new file/folder will be created as a precaution against entering the wrong password. After the decryption is complete, you can permanently delete the encrypted file/folder via a single command.

> *WARNING* :exclamation:
> -
> Even your password is wrong, the program will decrypt the file/folder and produce a result, *if it has a sufficient number of characters (byte number)*. In this case, be careful about deleting the encrypted file/folder since the decrypted one will be unreadable due to the wrong password. As for advice, always open and read the decrypted file/folder before you delete the encrypted one.

## Examples

Encryption process of a file

![enc_file](https://user-images.githubusercontent.com/45866787/193124480-0827db5a-3dc0-4e33-9c86-0972662f139b.png)

Decryption process of a file

![dec_file](https://user-images.githubusercontent.com/45866787/193124625-71160d5a-9f89-4f9f-a842-dadcc89399e5.png)

Encryption process of a folder

![enc_folder](https://user-images.githubusercontent.com/45866787/193124673-ce1f931a-848b-4d11-8a4f-945b917c839b.png)

Decryption process of a folder

![dec_folder](https://user-images.githubusercontent.com/45866787/193124688-11459f63-5d6d-45d5-88fb-aa732c9ea8c4.png)
