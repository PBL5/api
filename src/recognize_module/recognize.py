# Functions using for recognization with input from detected and cropped images

import os
import math
import numpy as np
from numpy import save
from sklearn.metrics.pairwise import euclidean_distances

import tensorflow.compat.v1 as tf
from cv2 import cv2

from global_config import PRETRAINED_MODEL_DIR, RAW_IMAGE_DIR
from src.recognize_module.libs import facenet, converter


def get_recognized_person_info(cropped, dem):
    
    # Cai dat cac tham so can thiet
    input_image_size = 160
    current_path = str(os.path.abspath(os.getcwd())) # .../AISrc
    length = len(current_path)
    current_path = current_path[:length-6] # ... /MiAI_Facerecog_2
    facenet_model_path = current_path + '/Models/20180402-114759.pb'

    with tf.Graph().as_default():

        # Cai dat GPU neu co
        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.6)
        sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))

        with sess.as_default():

            facenet.load_model(facenet_model_path)
            # Lay tensor input va output
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

            paths =  np.load(current_path + '/paths.npy')
            labels = np.load(current_path + '/labels.npy')
            emb_arrays = np.load(current_path + '/data.npy')

            recoged_name = ""
            while True:
                try:
                    scaled = cv2.resize(cropped, (input_image_size, input_image_size),interpolation=cv2.INTER_CUBIC)
                    scaled = facenet.prewhiten(scaled)
                    scaled_reshape = scaled.reshape(-1, input_image_size, input_image_size, 3)
                    feed_dict = {images_placeholder: scaled_reshape, phase_train_placeholder: False}
                    emb_array = sess.run(embeddings, feed_dict=feed_dict)
                            
                    # dùng L2 distance để đo khoảng cách L2 giữa 2 véctor
                    # [-1,1]
                    sim = euclidean_distances(emb_arrays, emb_array)
                    sim = np.squeeze(sim, axis = 1)
                    labels = np.where(sim == min(sim))
                    label = labels[0][0]


                    p = paths[label]
                    processed_path = current_path + "/Dataset/FaceData/processed/"
                    p = p[len(processed_path):]

                    str_arr = p.split('/')
                    person_name = str_arr[0]

                    dis = converter.Converter()
                    probability = dis.convert_dis2sim(min(sim))

                    if probability > 81:
                        recoged_name = person_name
                        print("Hinh: {}, Name: {}, Probability: {}".format(dem, person_name, probability))

                    # # Neu ty le nhan dang > 0.5 thi hien thi ten
                    # if probability > 70:
                    #     name = person_name
                    # else:
                    #     # Con neu <=0.5 thi hien thi Unknow
                    #     name = "Unknown"
                except Exception as exception:
                    print(exception)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                break

            return recoged_name
            cv2.destroyAllWindows()

def save_feature_vectors():
    #TODO: save to database instead binary
    #Get image, extract feature and save to binary

    current_path = str(os.path.abspath(os.getcwd()))  # .../AISrc
    facenet_model_path = current_path + PRETRAINED_MODEL_DIR

    processed_path = current_path + RAW_IMAGE_DIR
    with tf.Graph().as_default():
        # Cai dat GPU neu co
        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.6)
        sess = tf.Session(config=tf.ConfigProto(
            gpu_options=gpu_options, log_device_placement=False))
        with sess.as_default():
            facenet.load_model(facenet_model_path)
            # Lay tensor input va output
            images_placeholder = tf.get_default_graph().get_tensor_by_name(
                "input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name(
                "embeddings:0")
            phase_train_placeholder = tf.get_default_graph(
            ).get_tensor_by_name("phase_train:0")
            embedding_size = embeddings.get_shape()[1]

            print('Calculating features for images')
            dataset = facenet.get_dataset(processed_path)
            paths, labels = facenet.get_image_paths_and_labels(dataset)
            nrof_images = len(paths)
            nrof_batches_per_epoch = int(
                math.ceil(1.0 * nrof_images / 1000))
            emb_arrays = np.zeros((nrof_images, embedding_size))
            for i in range(nrof_batches_per_epoch):
                start_index = i * 1000
                end_index = min((i + 1) * 1000, nrof_images)
                paths_batch = paths[start_index:end_index]
                images = facenet.load_data(paths_batch, False, False, 160)
                feed_dict = {
                    images_placeholder: images,
                    phase_train_placeholder: False
                }
                # trả về danh sách embedded vectors
                emb_arrays[start_index:end_index, :] = sess.run(
                    embeddings, feed_dict=feed_dict)
        save(current_path + '/results/data.npy', emb_arrays)
        save(current_path + '/results/paths.npy', paths)
        save(current_path + '/results/labels.npy', labels)
    return emb_arrays
