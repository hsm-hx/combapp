from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=20)
    name_en = models.CharField(max_length=50)
    user_id = models.CharField(max_length=20)
    grade = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def is_4th_grade(self):
        return self.grade == 4

