# FolderLocker

Locking Files or Folders in Windows OS

(It may also work for other OS. However, it's not tested)

The FolderLocker system uses AES encryption. You can either create a key with 16, 24, and 32 bytes (In this process, the string object will turn into bytes) or generate a random key.

After you lock the folder, the program will change the binary data of the folder, and it will overwrite the files. To read/open the encrypted files, you'll need a key.

I have programmed the code so that when you decrypt the folder, a new folder will be created as a precaution against entering the wrong key.

After the decryption is complete, you can permanently delete the encrypted folder via a single command.

(Above procedures also applies for FileLocker)

>**WARNING**: Even if your key is wrong, the program will
decrypt the folder and produce a result, *if it has an acceptable byte number*. In this case, be careful about deleting the encrypted folder since the decrypted folder will be unreadable due to the wrong key. As for advice, always open and read the decrypted folder before you delete the encrypted one.

> **Note**: FolderLocker.exe and FileLocker.exe programs are based on overwriting your file/folder for encryption/decryption purposes. For this reason, if you have an anti-virus program, you may encounter a warning.

## Examples

### File Locker

A snapshot from the encryption process of a text file

![enc_filelock](https://user-images.githubusercontent.com/45866787/130692044-3bb6fd25-91be-4106-800b-d08243a844fa.png)

A snapshot from the decryption process of the same text file

![dec_filelock](https://user-images.githubusercontent.com/45866787/130692059-0eb1f1e6-2677-46fc-ba57-299a011ecc79.png)

### Folder Locker

A snapshot from the encryption process of a test folder

![enc_folderlock](https://user-images.githubusercontent.com/45866787/130692064-3b75b08c-6950-4301-80de-1e3d25f4f265.png)

A snapshot from the decryption process of a test folder

![dec_folderlock](https://user-images.githubusercontent.com/45866787/130692070-86e05e8b-9399-4c5a-af31-f784fdd16051.png)
