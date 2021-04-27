from django.db import models
import uuid

# Create your models here.
class UserType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name