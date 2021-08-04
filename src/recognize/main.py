import math
import os

import numpy as np
import tensorflow.compat.v1 as tf
from numpy import save

from . import facenet
from .preprocess_image import PreprocessImage

class RecognizeModule:
    processed_dir="/dataset/processed/"

    def __init__(self):
        self.image_path = r"test/imgTest.jpg"

    def export_feature_from_processed(self):
        current_path = str(os.path.abspath(os.getcwd()))  # .../AISrc
        facenet_model_path = current_path + '/models/20180402-114759.pb'

        processed_path = current_path + RecognizeModule.processed_dir
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

    def export_new_feature(self, name):
        # step1: crop
        current_path = str(os.path.abspath(os.getcwd()))  # .../AISrc
        length = len(current_path)
        current_path = current_path[:length - 6]  # ... /MiAI_Facerecog_2
        raw_path = current_path + RecognizeModule.processed_dir + name
        test = PreprocessImage()
        test.crop_and_save(raw_path, name)
        new_emb_arrays = self.export_feature_from_processed()
        return new_emb_arrays


    def initialize_all_featute(self):
        current_path = str(os.path.abspath(os.getcwd()))  # pbl5-api
        print(current_path)

        folder = current_path + RecognizeModule.processed_dir 
        sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
        print(sub_folders)

        for item in sub_folders:
            # step1: crop
            raw_path = folder + item
            test = PreprocessImage()
            test.crop_and_save(raw_path, item)
        self.export_new_feature(item)
