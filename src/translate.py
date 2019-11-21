from datetime import time
import yadisk
import requests

#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
DISK_URL = 'https://cloud-api.yandex.net/v1/disk/'
DISK_TOKEN = 'AgAAAAAA99WYAAXiekYaUe_L-UHlijsvnReoNYI'


def translate_it(from_lang, to_lang='ru'):
    text = input('Введите текст: ')
    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{from_lang}-{to_lang}'
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    print(json_)

    return json_


if __name__ == '__main__':

    translate_it('de')
