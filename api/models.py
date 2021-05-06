from django.db import models
import uuid

# Create your models here.
class UserType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

#User
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    usertype = models.ForeignKey(UserType, on_delete = models.CASCADE, null=True)
    def __str__(self):
        return self.name

#Subject
class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

#Date
class Date(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    def __str__(self):
        return self.date

#Class
class Class(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, null=True)
    teacher = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    def __str__(self):
        return self.name

#DateClass
class DateClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Date = models.ForeignKey(Date, on_delete = models.CASCADE, null=True)
    Class = models.ForeignKey(Class, on_delete = models.CASCADE, null=True)
    def __str__(self):
        return self.date

# DetailStudentAttentClass
class DetailStudentAttendClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    Class = models.ForeignKey(Class, on_delete = models.CASCADE, null=True)
    def __str__(self):
        return self.student


# StudentAttending
class StudentAttending(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isAttending = models.BooleanField()
    dateClass = models.ForeignKey(DateClass, on_delete = models.CASCADE, null=True)
    student = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    def __str__(self):
        return self.isAttending