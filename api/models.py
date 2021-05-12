from django.db import models
import uuid


class User_Types(models.Model):
    user_type_id = models.AutoField(
        primary_key=True, null=False, editable=False, unique=True)
    user_type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_type_name


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    user_type = models.ForeignKey(
        User_Types, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Class(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class DateClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.date


class DetailStudentAttendClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.student


class StudentAttending(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isAttending = models.BooleanField()
    dateClass = models.ForeignKey(
        DateClass, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.isAttending
