import pyAesCrypt
import os

def decryption(file, password):

    try:
        buffer_size = 512 * 1024
        pyAesCrypt.decryptFile(
            str(file),
            str(os.path.splitext(file)[0]),
            password,
            buffer_size
        )

        print("[Файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")
        
        os.remove(file)
    except BaseException:
        print("Неправильный ключ дешифрации!")