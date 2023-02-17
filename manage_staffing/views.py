import sys

from django.shortcuts import render

from django.template import Context, Template
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from manage_staffing.forms import LogInForm


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


def index(request):
    request.session['context']={}
    print("User")
    print(request.user)
    return render(request, 'manage_staffing/index.html')


def login_user(request):
    print('login request')
    print(request.method)
    if request.method=='POST':
        print("login post")
        print(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        print(f'username: {username}')
        print(f'password: {password}')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            print("We made a user")
            login(request, user)
            return render(request, 'manage_staffing/index.html')
        else:
            print("no user made")
            form=LogInForm()
            return render(request, 'manage_staffing/login.html')
    
    else:
            print("Going for the view")
            form=LogInForm()
            return render(request, 'manage_staffing/login.html',{'form': form})


@login_required()
def logout_user(request):
    logout(request)
    return render(request, 'manage_staffing/logout.html')

@login_required()
def persons(request):
    #get and show list of persons
    persons=Person.persons_context() # return a list of persons
    context={'persons' : persons}

    return render(request, 'manage_staffing/persons.html', context)

@login_required
def employers(request):
    #get and show the list of companies
    employers=Employer.employers_context()
    context={'employers':employers}

    return render(request, 'manage_staffing/employers.html', context)

@login_required
def jobs(request):
    #get and show the list of jobs
    jobs=Job.jobs_context()
    context={'jobs':jobs}

    return render(request, 'manage_staffing/jobs.html',context)

@login_required
def person(request, pk):
    person=Person.person_context(pk) # returns a tuple (person, [education] [skills])
    context={'person': person}
    return render(request, 'manage_staffing/person.html', context)

@login_required
def employer(request, pk):
    employer=Employer.employer_context(pk) # returns a tuple of (employer, [jobs])
    context={'employer': employer}
    return render(request, 'manage_staffing/employer.html', context)

@login_required
def job(request, pk):
    #get and show a job
    job=Job.job_context(pk) # returns a tuple (job, [requirements])
    context={'job': job}
    return render(request, 'manage_staffing/job.html', context)