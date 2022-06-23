import codecs

def verify(file):
    try:
        f = codecs.open(file, encoding='utf-8', errors='strict')
        for line in f:
            pass
    except UnicodeDecodeError:

        BLOCKSIZE = 1048576 # or some other, desired size in bytes
        with codecs.open(file, "r", "UTF-16") as sourceFile:
            with codecs.open(file, "w", "utf-8") as targetFile:
                while True:
                    contents = sourceFile.read(BLOCKSIZE)
                    if not contents:
                        break
                    targetFile.write(contents)