from django.db import models


class Board(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'boards'

    def __str__(self):
        return self.name

