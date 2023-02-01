# FFLocker

Locking files/folders [FF] in GNU/Linux via text-based user interface (TUI).

*The most important part of the algorithm is that during the locking process, your password is never saved on the computer and only displayed in the terminal for you to save it.*

## Description

FFLocker uses AES encryption. You can either create a password with 16, 24, and 32 characters (which corresponds to 128, 192, and 256 bits, respectively) or generate a random password with the help of the `secrets.choice`.

After you lock the file/folder, the program will change the binary data and overwrite it. To read/open the encrypted file/folder, you have to enter the password.

I have written the program in such a way that when you decrypt the file/folder, a new file/folder will be created as a precaution against entering the wrong password. At the end of the decryption process, you can permanently delete the encrypted file/folder via a single command (see the **WARNING** subsection).

Additionally, every file and folder receives `.enc` and `ENC` extensions at the end of the encryption process. If your pathname does not contain these extensions, the decryption process does not begin. Similarly, you cannot encrypt the file/folder if it has a `.enc` or `ENC` extension.

>### WARNING
>
>Even if your password is wrong, the program will decrypt the file/folder and produce a result *if it has a sufficient number of characters (bytes)*. In this case, be careful about deleting the encrypted file/folder since the decrypted one will be unreadable due to the wrong password. As for advice, always open and read the decrypted file/folder before you delete the encrypted one.

## Installation

You can install the FFLocker via `pip`

    python3 -m pip install fflocker

or by directly cloning to your desired directory

    git clone https://github.com/seVenVo1d/FFLocker.git

## Requirements

FFLocker requires `pycryptodome`, which can be installed by running

    python3 -m pip install pycryptodome

## User Guide

To start the *file locking* process run

    python3 -m fflocker.file_locker

Similarly, to start the *folder locking* process run

    python3 -m fflocker.folder_locker

from the terminal.

## Overview

Encryption process of a file         |  Decryption process of a file
:-------------------------:|:-------------------------:
![enc_file](https://user-images.githubusercontent.com/45866787/193124480-0827db5a-3dc0-4e33-9c86-0972662f139b.png)  |  ![dec_file](https://user-images.githubusercontent.com/45866787/193124625-71160d5a-9f89-4f9f-a842-dadcc89399e5.png)

Encryption process of a folder        |  Decryption process of a folder
:-------------------------:|:-------------------------:
![enc_folder](https://user-images.githubusercontent.com/45866787/193124673-ce1f931a-848b-4d11-8a4f-945b917c839b.png) | ![dec_folder](https://user-images.githubusercontent.com/45866787/193124688-11459f63-5d6d-45d5-88fb-aa732c9ea8c4.png)

## Upcoming Features

I am thinking to implement a command line interface (CLI), and it will probably look like this:

    $ fflocker -Fe [path]
    $ fflocker -De [path]
    $ fflocker -Fd [path]
    $ fflocker -Dd [path]

    -F --File
    -D --Directory
    -e --encrypt
    -d --decrypt
