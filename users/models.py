from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from . import requesting

# User = settings.AUTH_USER_MODEL
# Create your models here.

# Refreshed the models
# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()
#     height = models.FloatField()
#     weight = models.FloatField()

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('open', 'Open'),
    ('close', 'Close'),
    ('error', 'Error'),
    
)

all_status = (
    ('closed', 'Closed'),
    ('open', 'open')
)

department_choices = (
    ('pwslabdevops', 'PWSLab DevOps Support'),
    ('isupport', 'iSupport')
)

category_choices = (
    ('none', '-None-'),
    ('newproject_cicd_pipelinesetup', 'NEW Project CI/CD Pipeline Setup'),
    ('update_cicd_pipeline_configuration', 'Update CI/CD Pipeline Configuration'),
    ('descecops_pipeline_setup', 'DevSecOps Pipeline Setup'),
    ('cicd_pipeline_failure', 'CI/CD pipeline failure'),
    ('automated_deployment_failure', 'Automated Deployment failure'),
    ('docker_and_containers', 'Docker and Containers'),
    ('kubernetees_deployments', 'Kubernetes Deployments (like EKS/GCP)'),
    ('git_source_control', 'Git Source control'),
    ('pwslab_server_not_responding', 'PWSLab server not responding (502/503 errors)'),
    ('pwslab_runner_not_working', 'PWSLab Runner not working (jobs not running)'),
    ('usermanagement_project_access', 'User management and Project access'),
    ('cloud_integration_consultation', 'Cloud Integration Consultation - AWS/GCP/Azure'),
    ('others', 'Others')
)

priority = (
    ('none', '-None-'),
    ('high', 'High - Production System Down'),
    ('medium', 'Medium - System Impaired'),
    ('low', 'Low - General Guidance')
)

ticket_status = (
    ('created', 'Created'),
    ('open', 'Open'),
    ('close', 'Close'),
    ('error', 'Error'),
    
)


class Status(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, max_length=20)
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length = 254, default="")
    departments = models.CharField(choices=department_choices, default='pwslabdevops', max_length=20)
#     all_category_choices = forms.ChoiceField(choices=category_choices, widget=forms.Select(attrs={'class':'form-control'}))
#     pws_project_url = forms.URLField(max_length = 200, widget=forms.TextInput(attrs={'class':'form-control'}))
#     subject = forms.CharField(max_length = 120, widget=forms.TextInput(attrs={'class':'form-control'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
#     # # chocies = forms.ChoiceField(choices=ORDER_STATUS_CHOICES)
#     all_priority = forms.ChoiceField(choices=priority, widget=forms.Select(attrs={'class':'form-control'}))
#     all_ticket_status = forms.ChoiceField(choices=ticket_status, widget=forms.Select(attrs={'class':'form-control'}))

    def __str__(self):
        return self.user.username

    # @property
    # def check_status(self, save=False):
    #     # if self.status_1():
    #     #     print('created')
    #         return self.status

    # def status_1(self):
    #     return len(self.status) > 0 # True or False


    





