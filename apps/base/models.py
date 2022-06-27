from email.policy import default
from pyexpat import model
from django.db import models

class BaseModel(models.Model):
    """Model definition for BaseModel."""
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('state', default=True)
    created_date = models.DateField('date creation', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('date modification', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('date delete', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Models'


