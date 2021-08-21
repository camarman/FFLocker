# FolderLocker

Locking Files or Folders in Windows OS

(It may also work for other OS. However, it's not tested)

The FolderLocker system uses AES encryption. You can either create a key with 16, 24, and 32 bytes (In this process, the string object will turn into bytes) or generate a random key.

After you lock the folder, the program will change the binary data of the folder, and it will overwrite the files. To read/open the encrypted files, you'll need a key.

I have programmed the code so that when you decrypt the folder, a new folder will be created as a precaution against entering the wrong key.

After the decryption is complete, you can permanently delete the encrypted folder via a single command.

>**WARNING**: Even if your key is wrong, the program will
decrypt the folder and produce a result, *if it has an acceptable byte number*. In this case, be careful about deleting the encrypted folder since the decrypted folder will be unreadable due to the wrong key. As for advice, always open and read the decrypted folder before you delete the encrypted one.

> **Note**: FolderLocker.exe and FileLocker.exe programs are based on overwriting your file/folder for encryption/decryption purposes. For this reason, if you have an anti-virus program, you may encounter a warning.

## Examples

### File Locker

A snapshot from the encryption process of a text file

![enc_file](https://user-images.githubusercontent.com/45866787/130332397-6128f2e6-c5e8-45da-b100-5f67fbead6fe.png)

A snapshot from the decryption process of the same text file

![dec_file](https://user-images.githubusercontent.com/45866787/130332401-0d80f741-adf6-412d-a651-43713f838c83.png)

### Folder Locker

A snapshot from the encryption process of a test folder

![enc_folder](https://user-images.githubusercontent.com/45866787/130332404-d7994f63-a329-4e62-be24-14eb5bcb26fa.png)

A snapshot from the decryption process of a test folder

![dec_folder](https://user-images.githubusercontent.com/45866787/130332405-f1486188-7e88-4617-969d-bed46727cab6.png)
