from django.db import models
import uuid


class BaseModel(models.Model):
    "Defines base reusable fieldsfor every table"
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)


    class Meta:
        abstract = True
