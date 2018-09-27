from django.db import models
from django.conf import settings


# todo Подумать насчет запихивания модулей и уроков в json
class Course(models.Model):
    name = models.CharField(max_length=256, unique=True)
    # brief = models.CharField(max_length=256, null=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    duration = models.PositiveSmallIntegerField()
    start_date = models.DateTimeField()
    load = models.CharField(max_length=256)
    logo = models.ImageField(upload_to='images/courses/', null=True, blank=True)
    tutors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses')
    employers = models.ManyToManyField('Employer', related_name='courses')

    def __str__(self):
        return self.name

    def get_modules_names(self):
        return [module.name for module in self.modules.all()]

    def get_employers_names(self):
        return [employer.name for employer in self.employers.all()]


class Module(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.name


# todo Подумать насчет вынесения homework в отдельную модель
class Lesson(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    homework = models.TextField(null=True, blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.name


# todo Убрать blank из логотипа?
class Employer(models.Model):
    name = models.CharField(max_length=256)
    about = models.TextField()
    logo = models.ImageField(upload_to='images/employers/', blank=True)

    def __str(self):
        return self.name
