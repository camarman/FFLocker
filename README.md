# FolderLocker

Locking Files or Folders in Windows OS

(It may also work for other OS. However, it's not tested)

The FolderLocker system uses AES encryption. You can either create a key with 16, 24, and 32 bytes (In this process, the string object will turn into bytes) or generate a random key.

After you lock the folder, the program will change the binary data of the folder, and it will overwrite the files. To read/open the encrypted files, you'll need a key.

I have programmed the code so that when you decrypt the folder, a new folder will be created as a precaution against entering the wrong key.

After the decryption is complete, you can permanently delete the encrypted folder via a single command.

>**WARNING**: Even if your key is wrong, the program will
decrypt the encrypted folder and produce a result if it has an acceptable byte number. In this case, be careful about deleting the encrypted folder since the decrypted folder will be nob-readable due to the wrong key.

> **Note**: Since FolderLocker.exe or FileLocker.exe is trying to overwrite your file/folder for encryption/decryption purposes, you may encounter a warning, If you have an anti-virus program. In that case, you can always run the `.py` files.

## Examples

### File Locker

A snapshot from the encryption process of a pdf file

A snapshot from the decryption process of the same pdf file

### Folder Locker

A snapshot from the encryption process of a test folder

A snapshot from the decryption process of a test folder
