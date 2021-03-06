from django.db import models


class User_Types(models.Model):
    user_type_id = models.AutoField(
        primary_key=True, null=False, editable=False, unique=True
    )
    user_type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_type_name


class Users(models.Model):
    user_id = models.AutoField(
        primary_key=True, null=False, editable=False, unique=True
    )
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20, null=True)
    user_type = models.ForeignKey(
        User_Types, on_delete=models.CASCADE, null=False
    )
    gender = models.CharField(max_length=10, null=True)
    birthday = models.DateField(null=True)
    face_vectors = models.TextField(null=True)

    def __str__(self):
        return str(self.user_id)


class Subjects(models.Model):
    subject_id = models.AutoField(
        primary_key=True, null=False, editable=False, unique=True
    )
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name


class Classes(models.Model):
    class_id = models.AutoField(
        primary_key=True, null=False, editable=False, unique=True
    )
    subject = models.ForeignKey(
        Subjects, on_delete=models.CASCADE, null=True, blank=True
    )
    teacher = models.ForeignKey(
        Users, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.subject.subject_name


class Dates_Class(models.Model):
    id = models.AutoField(
        primary_key=True, null=False, editable=False, unique=True
    )
    date = models.DateField()
    course = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class Details_Student_Attend_Class(models.Model):
    detail_student_class_id = models.AutoField(
        primary_key=True, null=False, editable=False, unique=True
    )
    student = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.student.full_name


class StudentAttending(models.Model):
    id = models.AutoField(
        primary_key=True, null=False, editable=False, unique=True
    )
    isAttending = models.BooleanField()
    dateClass = models.ForeignKey(
        Dates_Class, on_delete=models.CASCADE, null=True
    )
    student = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class FileStore(models.Model):
    file = models.ImageField(upload_to='img/', null=True, blank=True)
