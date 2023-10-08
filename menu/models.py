from django.db import models


# Create your models here.
class MenuCats(models.Model):
    name = models.CharField(max_length=30)
    menu = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='sub')

    def __str__(self):
        return self.name
