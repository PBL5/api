# Main functions using for recognization of APIs

import os

from global_config import RAW_IMAGE_DIR

from src.recognize_module.detect import get_cropped_images
from src.recognize_module.utils import crop_and_save
from src.recognize_module.recognize import get_recognized_person_info, save_feature_vectors

def recognize_students_in_image(img_path):
    cropped_face_list = get_cropped_images(img_path)
    recog_faces = []
    for index, cropped_item in enumerate(cropped_face_list):
        person_name = get_recognized_person_info(cropped_item, index)
        if person_name != "":
            recog_faces.append(person_name)
    return recog_faces

def init_atribute_vectors():
    current_path = str(os.path.abspath(os.getcwd()))  # pbl5-api

    folder = current_path + RAW_IMAGE_DIR
    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]

    for sub_folder in sub_folders:
        raw_path = folder + sub_folder
        crop_and_save(raw_path, sub_folder)
        save_feature_vectors()
