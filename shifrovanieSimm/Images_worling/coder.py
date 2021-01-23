def encode(file, password):
    import pyAesCrypt

    bufferSize = 64 * 1024
    pyAesCrypt.encryptFile(str(file), str(file) + '.jpg', password, bufferSize)


def decode(file, password):
    import pyAesCrypt
    import os

    bufferSize = 64 * 1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)

from sys import platform
print(platform)