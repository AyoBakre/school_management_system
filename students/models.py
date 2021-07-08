from django.db import models
from random import randint

# Create your models here.


class BioData(models.Model):
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    phone_number = models.IntegerField(blank=True, null= True)
    email = models.EmailField(blank=True, null= True)
    parent_phone_number = models.IntegerField()
    parent_email = models.EmailField(blank=True, null= True)
    home_address = models.CharField(max_length=50)
    registration_number = 'KGC/2020/' + str(randint(1, 500))

    class_name = models.ForeignKey('ClassName', on_delete=models.PROTECT, null=True)
    dept = models.ForeignKey('Department', on_delete=models.PROTECT, null=True)
    class_teacher = models.ForeignKey('ClassTeacher', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.registration_number


class ClassName(models.Model):
    CLASS_IN_SCHOOL_CHOICES = (
        ('JSS1', 'Junior1'),
        ('JSS2', 'Junior2'),
        ('JSS3', 'Junior3'),
        ('SS1', 'Senior1'),
        ('SS2', 'Senior2'),
        ('SS3', 'Senior3'),
    )

    class_in_school = models.CharField(max_length=20, choices=CLASS_IN_SCHOOL_CHOICES,)

    def __str__(self):
        return self.class_in_school


class Department(models.Model):
    DEPARTMENT_CHOICES = (
        ('SCIENCE', 'Science'),
        ('ART', 'Art'),
        ('COMMERCIAL', 'Commercial'),
        ('None', 'None'),
    )

    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES,)

    def __str__(self):
        return self.department


class ClassTeacher(models.Model):
    TEACHER_CHOICES = (
        ('Mr Kesh', 'Mr Kesh'),
        ('Miss Moyo', 'Miss Moyo'),
        ('Mr Bukky', 'Mr Bukky'),
        ('Mr NathDare', 'Mr NathDare'),
        ('Mr Dare', 'Mr Dare'),
        ('Miss Magaret', 'Miss Magaret'),
        ('Mrs Onodare', 'Mrs Onodare'),
    )

    class_teachers = models.CharField(max_length=20, choices=TEACHER_CHOICES,)

    def __str__(self):
        return self.class_teachers

