# FolderLocker

Locking Files or Folders in Windows OS

(It may also work for other OS. However, it's not tested)

The FolderLocker system uses AES encryption. You can either create a key with 16, 24, and 32 bytes (In this process, the string object will turn into bytes) or generate a random key.

After you lock the folder, the program will change the binary data of the folder, and it will overwrite the files. To read/open the encrypted files, you'll need a key.

I have programmed the code so that when you decrypt the folder, a new folder will be created as a precaution against entering the wrong key.

After the decryption is complete, you can permanently delete the encrypted folder via a single command.

A cmd snapshot of the encryption process

![enc](https://user-images.githubusercontent.com/45866787/130187213-567f019a-1b08-4c77-b799-06797bdb4ee4.png)

A cmd snapshot of the decryption process

![dec](https://user-images.githubusercontent.com/45866787/130187230-d8bf8377-9101-49d4-add4-1e4161677079.png)
