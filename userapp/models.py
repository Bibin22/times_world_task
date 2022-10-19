from django.db import models
import uuid


class UserTable(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    CHOICES = (
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('Admin', 'Admin'),
        ('Editor', 'Editor'),
    )
    user_role = models.CharField(max_length=50, choices=CHOICES)
    mobile = models.CharField(max_length=10, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return str(self.name)


