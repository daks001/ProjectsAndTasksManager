from django import forms
from .models import ProjectsModel, TasksModel

# creating a form
class ProjectsForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = ProjectsModel
        # specify fields to be used
        fields = [
            "name",
            "description",
            "email",
            "creation",
            "completion",
            "status",
        ]

class TasksForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = TasksModel
        # specify fields to be used
        fields = [
            "name",
            "creation",
            "completion",
            "status",
            "project",
        ]