from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Status
from django.forms import ModelForm
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

class RegisterForm(UserCreationForm):
    username = forms.CharField(label = "User Name")
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

# class NameForm(forms.ModelForm):
#     name = forms.CharField(label='Your name', max_length=100)
#     email = forms.EmailField(label = "Email")
#     departments = forms.ChoiceField(choices=department_choices, widget=forms.Select(attrs={'class':'form-control'}))
#     all_category_choices = forms.ChoiceField(choices=category_choices, widget=forms.Select(attrs={'class':'form-control'}))
#     pws_project_url = forms.URLField(max_length = 200, widget=forms.TextInput(attrs={'class':'form-control'}))
#     subject = forms.CharField(max_length = 120, widget=forms.TextInput(attrs={'class':'form-control'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
#     # # chocies = forms.ChoiceField(choices=ORDER_STATUS_CHOICES)
#     all_priority = forms.ChoiceField(choices=priority, widget=forms.Select(attrs={'class':'form-control'}))
#     all_ticket_status = forms.ChoiceField(choices=ticket_status, widget=forms.Select(attrs={'class':'form-control'}))

    # class Meta:
        # model = Status
        # fields = [
        #     'name',
        #     'email',
        #     'departments',
        #     'all_category_choices',
        #     'pws_project_url',
        #     'subject',
        #     'description',
        #     'all_priority',
        #     'all_ticket_status',
        # ]

    
class ContractForm(ModelForm):
    class Meta:
        model = Status
        fields = [
            # 'status',
            'name',
            'email',
            'departments',
            # 'all_category_choices',
            # 'pws_project_url',
            # 'subject',
            # 'description',
            # 'all_priority',
            # 'all_ticket_status',
        ]

        # def __init__(self, *args, **kwargs):
        #     super(ContractForm, self).__init__(*args, **kwargs)

# just refreshed the models
# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = [
#             'name',
#             'age',
#             'height',
#             'weight',
#         ]


