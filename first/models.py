from django.db import models


class FileModel(models.Model):
    file = models.FileField(upload_to='file/')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
