from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    major = models.CharField(max_length=255, null=False, blank=False)
    year_of_study = models.IntegerField(null=False, blank=False)
    faculty = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'ID: {self.id} {self.name}'