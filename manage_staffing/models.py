from django.db import models

# Create your models here.
class Ed_Major(models.Model):
    major=models.CharField(max_length=30)

    def __str__(self):
        return self.major

class Ed_Level(models.Model):
    level=models.CharField(max_length=30)

    def __str__(self):
        return self.level

class Classification(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Expertise(models.Model):
    LEVEL=models.TextChoices('Level', 'Entry Junior Middle Senior Expert')
    level=models.CharField(max_length=30, choices=LEVEL.choices)

    def __str__(self):
        return self.level

class Education(models.Model):
    ed_major=models.ForeignKey(Ed_Major, on_delete=models.CASCADE)
    ed_level=models.ForeignKey(Ed_Level, on_delete=models.CASCADE)

    def __str__(self):
        return (self.ed_level.level + ": " + self.ed_major.major)

class Field(models.Model):
    name=models.CharField(max_length=30)
    classification=models.ForeignKey(Classification, on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.classification.name + ": " + self.name)

class Skill(models.Model):
    field=models.ForeignKey(Field, on_delete=models.CASCADE)
    expertise=models.ForeignKey(Expertise, on_delete=models.CASCADE)

    def __str__(self):
        return (self.field.name + ": " + self.expertise.level)

class Requirement(models.Model):
    skill=models.ForeignKey(Skill, on_delete=models.CASCADE)
    education=models.ForeignKey(Education, on_delete=models.CASCADE)

    def __str__(self):
        return (self.skill.field.name + ": " + self.skill.expertise.level + ": " + self.education.ed_level.level + ": " +  self.education.ed_major.major)

class Employer(models.Model):
    name=models.CharField(max_length=50)
    identifier=models.CharField(max_length=10)

    def __str__(self):
        return (self.identifier + ": " + self.name)

    def employers_context():
        employers=Employer.objects.all()
        return employers

    def employer_context(pk):
        employer=Employer.objects.get(pk=pk)
        jobs=list(Job.objects.filter(employer=pk)) # return list of jobs by the specified employer
        print("Jobs")
        print(jobs)
        return (employer, jobs)

    

class Person(models.Model):
    name=models.CharField(max_length=50)
    identifier=models.CharField(max_length=10)
    educations=models.ManyToManyField(Education)
    skills=models.ManyToManyField(Skill)

    def __str__(self):
        return (self.identifier + ": " + self.name)

    def persons_context():
        persons=Person.objects.all()
        return persons

    def person_context(pk):
        person=Person.objects.get(pk=pk)
        print("Person")
        print(person.name)
        print(person.identifier)
        print(list(person.educations.all())[0].ed_major.major)
        print(list(person.skills.all())[0].field.name)
        return (person, list(person.educations.all()), list(person.skills.all()))
    

class Job(models.Model):
    title=models.CharField(max_length=50)
    employer=models.ForeignKey(Employer, on_delete=models.CASCADE)
    requirements=models.ManyToManyField(Requirement)

    def __str__(self):
        return (self.employer.name + ": " + self.title)

    def jobs_context():
        jobs=Job.objects.all()
        return jobs

    def job_context(pk):
        job=Job.objects.get(pk=pk)
        requirements=list(job.requirements.all())
        r_list=[]
        for r in requirements:
            name=r.skill.field.name
            classification=r.skill.field.classification
            expertise=r.skill.expertise
            level=r.education.ed_level
            major=r.education.ed_major
            r_list.append((name,classification, expertise, level, major))
        return (job, r_list)


