from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # # уже есть id, username, password, first_name, last_name, email,
    # # is_superuser, is_staff, is_active, last_login, date_joined
    # father_name = models.CharField(max_length=150, blank=True)
    # birthday = models.DateField(blank=True)
    # phone = models.CharField(max_length=15, blank=True, unique=True)
    # ship_address = models.CharField(max_length=255, blank=True)
    # is_anonymous = models.BooleanField(default=False)  # is_anonymous занято каким-то методом и джанго ругается

    def __str__(self):
        return self.username
