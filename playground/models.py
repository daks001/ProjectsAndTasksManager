from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime

StatusChoices = [
    ("ACTIVE", "Active"),
    ("INACTIVE", "Inactive"),
    ("COMPLETE", "Complete"),
]

# Create your models here.
class ProjectsModel(models.Model):
    # fields of the model
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    email = models.EmailField()
    creation = models.DateField(_("Date"), default=datetime.today)
    completion = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=8,
        choices=StatusChoices,
        default="INACTIVE"
    )
    # renames the instances of the model with their name
    def __str__(self):
        return self.name

class TasksModel(models.Model):
    # fields of the model
    name = models.TextField(unique=True)
    creation = models.DateField(_("Date"), default=datetime.today)
    completion = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=8,
        choices=StatusChoices,
        default="INACTIVE"
    )
    project = models.ForeignKey(ProjectsModel, on_delete=models.CASCADE)
    # renames the instances of the model with their name
    def __str__(self):
        return self.name