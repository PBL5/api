import detect
import face_reg_img2
import numpy as np
import matplotlib.pyplot as plt

class Recog_Module:
    def __init__(self):
        self.cropped = r"test\\imgTest.jpg"

    def Recog_Process(self, img_path):
        mtcnn_detect = detect.MTCNN_Detect()
        recog = face_reg_img2.FaceRecog()

        cropped_face_list = mtcnn_detect.main(img_path)
        recog_faces = []
        dem = 1
        for cropped_item in cropped_face_list:
            person_name = recog.main(cropped_item, dem)
            if person_name != "":
                recog_faces.append(person_name)
            dem = dem + 1
        return recog_faces
            
# r = Recog_Module()
# r.Recog_Process( r"/home/leo/global/pbl5/pbl5-api/test/4.jpg")
