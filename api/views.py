import os
from datetime import date

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response

from src.recognize_module.main import init_atribute_vectors, recognize_students_in_image

from .models import Classes, Dates_Class, Details_Student_Attend_Class, User_Types, Users
from .serializer import (
    AddStudentSerializer, ClassSerializer, LoginSerializer,
    StudentFilterSerializer, UserSerializer
)


class StudentAPIView(generics.GenericAPIView):
    @swagger_auto_schema(request_body=StudentFilterSerializer)
    def post(self, request):
        class_id = request.data['class_id']

        students = Users.objects.filter(
            details_student_attend_class__course__pk=class_id
        )

        if 'filter_options' in request.data:
            filter_options = request.data['filter_options']
            if 'gender' in filter_options:
                students = students.filter(gender=filter_options['gender'])

            if 'full_name' in filter_options:
                students = students.filter(
                    full_name__icontains=filter_options['full_name']
                )

            if 'email' in filter_options:
                students = students.filter(
                    email__icontains=filter_options['email']
                )

            if 'student_id' in filter_options:
                students = students.filter(
                    user_id=filter_options['student_id']
                )

            if 'birthday' in filter_options:
                students = students.filter(birthday=filter_options['birthday'])

        serializer = UserSerializer(students, many=True)
        return Response(serializer.data)


class AttendanceAPIView(generics.GenericAPIView):
    class_id_param = openapi.Parameter(
        'class_id', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[class_id_param])
    def get(self, request):
        class_id = request.query_params['class_id']

        today = date.today()

        students = Users.objects.filter(
            studentattending__dateClass__course__pk=class_id,
            studentattending__dateClass__date=today
        )

        serializer = UserSerializer(students, many=True)
        return Response(serializer.data)


class ClassAPIView(generics.GenericAPIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)


class LoginAPIView(generics.GenericAPIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        try:
            user = Users.objects.get(email=email)

            # Check user logging in is teacher
            if user.user_type_id != 2:
                return HttpResponse('Only teacher can login', status=401)

            if user.password == password:
                serializer = UserSerializer(user)
                return Response(serializer.data)
            return HttpResponse('Password incorrect.', status=401)
        except ObjectDoesNotExist:
            return HttpResponse('User doesn\'t exist', status=401)


class RecognizeAPIView(generics.CreateAPIView):
    class_id_param = openapi.Parameter(
        'class_id', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[class_id_param])
    def get(self, request, *args, **kwargs):
        # print('start', request.query_params)
        # class_id = request.query_params['class_id']

        # today = date.today()
        # course = Classes.objects.get(pk=class_id)
        # date_class = {}
        # try:
        #     date_class = Dates_Class.objects.get(date=today, course=course)
        # except Dates_Class.DoesNotExist:
        #     date_class = Dates_Class.objects.create(date=today, course=course)

        #  img_path = self.save_file()

        current_path = str(os.path.abspath(os.getcwd()))  # .../AISrc
        img_path = current_path + '/dataset/test/HQT/9.jpg'

        recoged_faces = recognize_students_in_image(img_path)
        print(recoged_faces)

        # for user_id in recoged_faces:
        #     user_id = int(user_id)
        #     student = Users.objects.get(pk=user_id)

        #     exist_attendances = StudentAttending.objects.filter(
        #         student__pk=user_id, dateClass__pk=date_class.id).count()

        #     if exist_attendances == 0:
        #         print(user_id, 'not exist')
        #         StudentAttending.objects.create(isAttending=True,
        #                                         dateClass=date_class,
        #                                         student=student)

        print(recoged_faces)
        return Response()


class AddStudentAPIView(generics.GenericAPIView):
    @swagger_auto_schema(request_body=AddStudentSerializer)
    def post(self, request):
        #  Comment following 23 lines if you want to create trained file with the existing dataset
        full_name = request.data['full_name']
        email = request.data['email']
        birthday = request.data['birthday']
        gender = request.data['gender']

        student_user_type = User_Types.objects.get(pk=1)
        user = Users.objects.create(
            full_name=full_name,
            email=email,
            birthday=birthday,
            gender=gender,
            user_type=student_user_type
        )

        # current_path = str(os.path.abspath(os.getcwd()))  # .../AISrc
        # length = len(current_path)
        # current_path = current_path[:length - 6]
        # folder_contain_img_path = current_path + '/Dataset/FaceData/raw/' + str(
        #     user.user_id) + '/'
        # os.mkdir(folder_contain_img_path)

        # for i in range(20):
        #     self.save_file(folder_contain_img_path)

        #  face_net.export_new_feature(str(user.user_id))
        #  face_net.initialize_all_featute()
        #  return Response('thành công!')


class InitStudentAPIView(generics.GenericAPIView):
    def get(self, request):
        users_info: [dict] = [
            {
                'full_name': 'Trang',
                'email': 'trang@pbl5.net',
                'birthday': '2000-01-01',
                'gender': 'female'
            }, {
                'full_name': 'Huyen',
                'email': 'huyen@pbl5.net',
                'birthday': '2000-01-01',
                'gender': 'female'
            }, {
                'full_name': 'Quynh',
                'email': 'quynh@pbl5.net',
                'birthday': '2000-01-01',
                'gender': 'female'
            }
        ]

        student_user_type: User_Types = User_Types.objects.get(user_type_id=1)
        course: Classes = Classes.objects.get(subject_id=1)
        for user_info in users_info:
            try:
                Users.objects.get(email=user_info['email'])
            except Users.DoesNotExist:
                student: Users = Users.objects.create(
                    full_name=user_info['full_name'],
                    email=user_info['email'],
                    birthday=user_info['birthday'],
                    user_type=student_user_type,
                    gender=user_info['gender']
                )

                Details_Student_Attend_Class.objects.create(
                    course_id=course.pk, student_id=student.pk
                )

        init_atribute_vectors()
        return Response()
