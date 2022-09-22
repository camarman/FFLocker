# FFLocker

Locking files or folders in Linux (it may also work in Windows, however it's not tested). The program can encrypt these file extensions and more;

    .jpg, .txt, .pdf, .xlsx, .ppt/pptx, .docx, .png, .py, .wav, .m4a

## Installation

Clone the repository via

    git clone https://github.com/seVenVo1d/folder_locker.git

To install the required packages for FFLocker type

    python3 -m pip install -r requirements.txt

## Description

FFLocker uses AES encryption. You can either create a password with 16, 24, and 32 characters (which corresponds to 128, 192, 256 bits, respectively) or generate a random password with the help of the `secrets.choice`. The most important part of the algorithm is that during the locking process, your password is never saved on the computer and only displayed in the terminal for you to save it.

After you lock the file/folder, the program will change the binary data of the file/folder, and it will overwrite the files. To read/open the encrypted files, you have to enter the password.

I have programmed the code so that when you decrypt the file/folder, a new file/folder will be created as a precaution against entering the wrong password. After the decryption is complete, you can permanently delete the encrypted file/folder via a single command.

>WARNING :exclamation: Even your password is wrong, the program will decrypt the file/folder and produce a result, *if it has a sufficient number of characters (byte number)*. In this case, be careful about deleting the encrypted file/folder since the decrypted one will be unreadable due to the wrong password. As for advice, always open and read the decrypted file/folder before you delete the encrypted one.

## Examples

### File Locker

A snapshot from the encryption process of a text file

A snapshot from the decryption process of the same text file

### Folder Locker

A snapshot from the encryption process of a test folder

A snapshot from the decryption process of a test folder
