from django.db import models

# todo Добавить связь работодателей с курсами
# todo Добавить связь преподавателей с курсами


# todo Подумать насчет запихивания модулей и уроков в json
class Course(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    duration = models.PositiveSmallIntegerField()
    start_date = models.DateTimeField()
    load = models.TextField()
    logo = models.ImageField(upload_to='images/courses/')
    

class Module(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')


# todo Подумать насчет вынесения homework в отдельную модель
class Lesson(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)
    date = models.DateTimeField()
    homework = models.TextField(null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')


class Employer(models.Model):
    name = models.CharField(max_length=256)
    about = models.TextField()
    logo = models.ImageField(upload_to='images/employers/')
