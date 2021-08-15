import os
import random
import re
import string
import requests

from global_config import RASP_API_ENTRY_POINT

FILE_NAME_LENGTH = 10

def get_image_from_rasp():
    current_path = str(os.path.abspath(os.getcwd()))  # .../AISrc
    response = requests.get(RASP_API_ENTRY_POINT + 'capture')

    response_file_name = re.findall(
        'filename=(.+)', response.headers['content-disposition'])[0]
    ext = os.path.splitext(response_file_name)

    file_name = ''.join(
        random.choices(string.ascii_lowercase + string.digits,
                       k=FILE_NAME_LENGTH))

    img_path = current_path + '/img/' + file_name + ext[1][:-1]
    with open(img_path, 'wb') as f:
        f.write(response.content)

    return img_path
