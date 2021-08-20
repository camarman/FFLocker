# FolderLocker

Locking Files or Folders in Windows OS

(It may also work for other OS. However, it's not tested)

The FolderLocker system uses AES encryption. You can either create a key with 16, 24, and 32 bytes (In this process, the string object will turn into bytes) or generate a random key.

After you lock the folder, the program will change the binary data of the folder, and it will overwrite the files. To read/open the encrypted files, you'll need a key.

I have programmed the code so that when you decrypt the folder, a new folder will be created as a precaution against entering the wrong key.

After the decryption is complete, you can permanently delete the encrypted folder via a single command.

A snapshot of the encryption process for a pdf file

![filelocker](https://user-images.githubusercontent.com/45866787/130237326-3cf06735-c1c1-449d-8fb3-a609715d0d68.png)


A snapshot of the decryption process for the same pdf.

![decry](https://user-images.githubusercontent.com/45866787/130237348-fc24783e-bb19-4d6d-9e0b-7fc72a5f3197.png)
