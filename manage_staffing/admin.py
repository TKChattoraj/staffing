from django.contrib import admin
from manage_staffing.models import (
    Ed_Major,
    Ed_Level,
    Classification,
    Expertise,
    Education,
    Field,
    Skill,
    Requirement,
    Employer,
    Person, 
    Job
)


# Register your models here.
models=[Ed_Major,
    Ed_Level,
    Classification,
    Expertise,
    Education,
    Field,
    Skill,
    Requirement,
    Employer,
    Person, 
    Job]
admin.site.register(models)