from django.test import TestCase
from django.urls import reverse

from api.models import Classes, Details_Student_Attend_Class, Subjects, User_Types, Users


class SearchStudentTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(SearchStudentTestCase, cls).setUpClass()

        cls.search_student_url = '/api/students'

        student_user_type = User_Types.objects.create(user_type_name='Student')
        teacher_user_type = User_Types.objects.create(user_type_name='Teacher')

        student1 = Users.objects.create(full_name='User 1',
                                        email='user1@abc.com',
                                        birthday='2000-05-07',
                                        gender='male',
                                        user_type=student_user_type)

        student2 = Users.objects.create(full_name='User 2',
                                        email='user2@abc.com',
                                        birthday='2000-06-07',
                                        gender='female',
                                        user_type=student_user_type)

        student3 = Users.objects.create(full_name='User 3',
                                        email='user3@abc.com',
                                        birthday='2000-06-08',
                                        gender='male',
                                        user_type=student_user_type)

        teacher1 = Users.objects.create(full_name='User 4',
                                        email='user4@abc.com',
                                        birthday='1976-06-08',
                                        gender='male',
                                        user_type=teacher_user_type)

        ai_subject = Subjects.objects.create(subject_name='AI')
        Subjects.objects.create(subject_name='Algorithm')

        ai_class = Classes.objects.create(subject=ai_subject, teacher=teacher1)

        Details_Student_Attend_Class.objects.create(student=student1,
                                                    course=ai_class)
        Details_Student_Attend_Class.objects.create(student=student2,
                                                    course=ai_class)

    def test_empty_classid(self):
        response = self.client.post(self.search_student_url)

        self.assertEqual(response.status_code, 400)

    def test_search_with_class_id(self):
        response = self.client.post(self.search_student_url, {'class_id': 1})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['user_id'], 1)
        self.assertEqual(response.data[1]['user_id'], 2)

    def test_search_with_full_name(self):
        data = {'class_id': '1', 'filter_options': {'full_name': 'user 1'}}
        response = self.client.post('/api/students', data, format='json')

        self.assertEqual(response.status_code, 200)
        #  self.assertEqual(len(response.data), 1)
        #  self.assertEqual(response.data[0]['user_id'], 1)

    def test_search_with_email(self):
        return

    def test_search_with_birthday(self):
        return

    def test_search_with_gender(self):
        return

    def test_search_with_user_type(self):
        return
