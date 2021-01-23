class EnDeCoder:
    source = u''
    key = ''
    geo_Geted = False
    geoloc = False

    # значение переменной source - unicode текст, key - обычная строка
    def __init__(self, source: str = u'qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM.,'
                                     u'йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛД'
                                     u'ЖЭЁЯЧСМИТЬБЮ',
                 key: str = '1234567890'):
        self.source = source
        self.key = '1234567890.12 1234567890.12'

    # получение геолокации
    def geolocation(self):

        # import
        from bs4 import BeautifulSoup
        from selenium import webdriver
        import time
        import os
        from urllib.parse import urljoin

        # проверка на то, что геолокация уже получена
        if self.geo_Geted == True:
            return self.geoloc
        self.geo_Geted = True

        # файл с html
        fileN = 'geo.html'
        url = urljoin('file://', os.path.abspath(fileN))

        # создание драйвера на основе Chrome
        driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))
        driver.get(url)
        time.sleep(5)

        # обращение к окну браузера, парсинг геолокации
        soup = BeautifulSoup(driver.page_source, "html.parser")
        data = str(soup.p.text).split(' ')
        geoData = []
        driver.close()

        # проверяем доступ к геолокации
        try:
            datao = data[1].split('.')
            do = str(datao[0]) + str(datao[1][:2])
            datat = data[3].split('.')
            dt = str(datat[0]) + str(datat[1][:2])
            print(do + dt)
            self.geoloc = do + dt
            return do + dt
        except:
            print('Ошибка')
            exit()
            return 'error'

    # превращение двух параметров геолокации в одну строку
    def to_geo_data(self, geolocation):
        geolocation = geolocation.split()
        datao = geolocation[0].split('.')
        do = str(datao[0]) + str(datao[1][:2])
        datat = geolocation[1].split('.')
        dt = str(datat[0]) + str(datat[1][:2])
        return do + dt

    # utf данная функция кодирует символ - для строки лучше не использовать
    # (это будет простым шифром Цезаря - кодирует линейно)
    def encode(self, text, step):
        return text.translate(
            str.maketrans(self.source, self.source[step:] + self.source[:step])
        )

    # utf данная функция декодирует символ - для строки лучше не использовать
    # (это будет простым шифром Цезаря - кодирует линейно)
    def decode(self, text, step):
        return text.translate(
            str.maketrans(self.source[step:] + self.source[:step], self.source)
        )

    # utf данная функция кодирует строку
    def full_encode(self, text):
        self.key = self.geolocation()

        output = []

        for i in range(len(text)):
            if int(self.key[i % int(len(self.key))]) % 2 == 0:
                output.append(self.encode(text[i],
                                          int(self.key[i % int(len(self.key))]) * (1)))
            else:
                output.append(self.encode(text[i],
                                          int(self.key[i % int(len(self.key))]) * (-1)))

        return ''.join(output)

    def full_encode_by_new_key(self, text, key):
        key = self.to_geo_data(key)
        output = []

        for i in range(len(text)):
            if int(key[i % int(len(key))]) % 2 == 0:
                output.append(self.encode(text[i], int(key[i % int(len(key))]) * (1)))
            else:
                output.append(self.encode(text[i], int(key[i % int(len(key))]) * (-1)))

        return ''.join(output)

    # utf данная функция декодирует строку
    def full_decode(self, text):
        self.key = self.geolocation()

        output = []

        for i in range(len(text)):
            if int(self.key[i % int(len(self.key))]) % 2 == 0:
                output.append(self.decode(text[i],
                                          int(self.key[i % int(len(self.key))]) * (1)))
            else:
                output.append(self.decode(text[i],
                                          int(self.key[i % int(len(self.key))]) * (-1)))

        return ''.join(output)

    # utf данная функция кодирует файл, с использованием алгоритма функции full_encode
    def file_encode(self, input_path, output_path):
        r = open(input_path, 'r', encoding='utf-8')
        w = open(output_path, 'w', encoding='utf-8')
        rr = r.read()
        rre = self.full_encode(rr)

        w.write(rre)
        r.close()
        w.close()

        return 'Файл зашифрован'

    def file_encode_by_new_key(self, input_path, output_path, key):
        r = open(input_path, 'r', encoding='utf-8')
        w = open(output_path, 'w', encoding='utf-8')
        rr = r.read()
        rre = self.full_encode_by_new_key(rr, key)

        w.write(rre)
        r.close()
        w.close()

        return 'Файл зашифрован'

    # utf данная функция декодирует файл, с использованием алгоритма функции full_decode
    def file_decode(self, input_path, output_path):
        w = open(input_path, 'r', encoding='utf-8')
        rw = open(output_path, 'w', encoding='utf-8')
        wr = w.read()
        wrd = self.full_decode(wr)

        rw.write(wrd)
        w.close()
        rw.close()

        return 'Файл расшифрован'

    # данная функция может кодировать файл, практически, любого разрешения
    def encode_other_files(self, file):
        import pyAesCrypt

        bufferSize = 64 * 1024
        pyAesCrypt.encryptFile(str(file), str(file) + '.' + file.split('.')[-1],
                               self.geolocation(), bufferSize)

    # данная функция может кодировать файл, практически, любого разрешения
    def encode_other_files_by_new_key(self, file, key):
        import pyAesCrypt

        bufferSize = 64 * 1024
        pyAesCrypt.encryptFile(str(file), str(file) + '.' + file.split('.')[-1],
                               self.to_geo_data(key), bufferSize)

    # данная функция может расдировать файл, практически, любого разрешения
    def decode_other_files(self, file):
        import pyAesCrypt
        import os

        bufferSize = 64 * 1024
        pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]),
                               self.geolocation(), bufferSize)

coder = EnDeCoder()
coder.decode_other_files('test.txt.txt')