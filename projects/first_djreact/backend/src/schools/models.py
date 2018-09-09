from django.db import models


class School(models.Model):
    school_name = models.TextField()

    def __str__(self):
        return self.school_name
