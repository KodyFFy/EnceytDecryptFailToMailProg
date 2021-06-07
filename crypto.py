import pyAesCrypt
import os

def encryption(file, password):

    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + "(Зашифрованный)",
        password,
        buffer_size
    )

    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    os.remove(file)