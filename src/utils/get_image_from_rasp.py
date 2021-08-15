import os
import random
import re
import string
import requests

from global_config import RASP_API_ENTRY_POINT

FILE_NAME_LENGTH = 10

def get_image_from_rasp():
    current_path: str = str(os.path.abspath(os.getcwd()))  # .../AISrc
    response: requests.Response = requests.get(RASP_API_ENTRY_POINT + 'capture')

    response_file_name: str = re.findall(
        'filename=(.+)', response.headers['content-disposition'])[0]
    ext: str = os.path.splitext(response_file_name)

    file_name: str = ''.join(
        random.choices(string.ascii_lowercase + string.digits,
                       k=FILE_NAME_LENGTH))

    img_path: str = current_path + '/img/' + file_name + ext[1][:-1]
    with open(img_path, 'wb') as image:
        image.write(response.content)

    return img_path
