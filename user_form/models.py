from django.utils import timezone
from django.db import models


class UserForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = ('User Form')
        verbose_name_plural = ('User Forms')

    def __str__(self) -> str:
        return f"{self.email}"
