# FolderLocker

Locking Files or Folders in Windows OS

(It may also work for other OS. However, it's not tested)

The FolderLocker system uses AES encryption. You can either create a key with 16, 24, and 32 bytes (In this process, the string object will turn into bytes) or generate a random key.

After you lock the folder, the program will change the binary data of the folder, and it will overwrite the files. To read/open the encrypted files, you'll need a key.

I have programmed the code so that when you decrypt the folder, a new folder will be created as a precaution against entering the wrong key.

After the decryption is complete, you can permanently delete the encrypted folder via a single command.

>Note: Since Folder Locker.exe or File Locker.exe is trying to overwrite your file/folder for encryption/decryption purposes, you may encounter a warning, If you have an anti-virus program. If running  `.exe` does not feel safe, you can always run the `.py` files.

## Examples

### File Locker

A snapshot from the encryption process of a pdf file

![filelocker](https://user-images.githubusercontent.com/45866787/130237326-3cf06735-c1c1-449d-8fb3-a609715d0d68.png)

A snapshot from the decryption process of the same pdf file

![decry](https://user-images.githubusercontent.com/45866787/130237348-fc24783e-bb19-4d6d-9e0b-7fc72a5f3197.png)

### Folder Locker

A snapshot from the encryption process of a test folder

![end_folder](https://user-images.githubusercontent.com/45866787/130242453-90420264-c120-4430-b4f0-ccc24e9caf4b.png)

A snapshot from the decryption process of a test folder

![dec_folder](https://user-images.githubusercontent.com/45866787/130242624-7efeafe4-3606-45cb-bad4-83548d8df582.png)
