from django.db import models
from django.urls import reverse
# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=100)
    lives_in = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("friends:friend-detail", kwargs={"id": self.id})
