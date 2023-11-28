from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f'รหัสวิชา {self.id} ชื่อรายวิชา {self.name}'