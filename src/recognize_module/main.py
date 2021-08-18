# Main functions using for recognization of APIs

from array import array
import os

from global_config import PROCESSED_IMAGE_DIR_SUFFIX, RAW_IMAGE_DIR_SUFFIX

from src.recognize_module.detect import get_cropped_images
from src.recognize_module.utils import crop_and_save
from src.recognize_module.recognize import get_recognized_person_info, save_feature_vectors


def recognize_students_in_image(img_path: str):
    # recognize students
    # params:
    #   img_path: path of image
    # return: list of person name

    cropped_face_list: array = get_cropped_images(img_path)
    recog_faces: array = []
    for index, cropped_item in enumerate(cropped_face_list):
        person_name = get_recognized_person_info(cropped_item, index)
        if person_name != "":
            recog_faces.append(person_name)
    return recog_faces


def init_atribute_vectors():
    # init attribute vectors from images in dataset

    current_path = str(os.path.abspath(os.getcwd()))  # pbl5-api

    raw_image_dir = current_path + RAW_IMAGE_DIR_SUFFIX
    processed_image_dir = current_path + PROCESSED_IMAGE_DIR_SUFFIX
    sub_folders = [
        name for name in os.listdir(raw_image_dir)
        if os.path.isdir(os.path.join(raw_image_dir, name))
    ]

    for sub_folder in sub_folders:
        raw_path = raw_image_dir + "/" + sub_folder
        processed_path = processed_image_dir + "/" + sub_folder
        crop_and_save(raw_path, sub_folder)
    save_feature_vectors()
