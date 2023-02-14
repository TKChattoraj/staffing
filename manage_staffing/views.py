import sys

from django.shortcuts import render

from django.template import Context, Template
from django.core import serializers


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
    return render(request, 'manage_staffing/index.html')


def persons(request):
    #get and show list of persons
    persons=Person.persons_context() # return a list of persons
    context={'persons' : persons}

    return render(request, 'manage_staffing/persons.html', context)


def employers(request):
    #get and show the list of companies
    employers=Employer.employers_context()
    context={'employers':employers}

    return render(request, 'manage_staffing/employers.html', context)

def jobs(request):
    #get and show the list of jobs
    jobs=Job.jobs_context()
    context={'jobs':jobs}

    return render(request, 'manage_staffing/jobs.html',context)


def person(request, pk):
    person=Person.person_context(pk) # returns a tuple (person, [education] [skills])
    context={'person': person}
    return render(request, 'manage_staffing/person.html', context)

def employer(request, pk):
    employer=Employer.employer_context(pk) # returns a tuple of (employer, [jobs])
    context={'employer': employer}
    return render(request, 'manage_staffing/employer.html', context)


def job(request, pk):
    #get and show a job
    job=Job.job_context(pk) # returns a tuple (job, [requirements])
    context={'job': job}
    return render(request, 'manage_staffing/job.html', context)