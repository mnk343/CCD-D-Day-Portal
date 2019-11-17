from multiselectfield import MultiSelectField
from django.db import models
from django.shortcuts import reverse
# from django.contrib.auth.models import User
from users.models import CustomUser

programme = (
        ('btech' , 'btech') ,
        ('mtech' , 'mtech') ,
        ('msc' , 'msc') ,
        ('mdes' , 'mdes') ,
        ('bdes' , 'bdes') ,
        ('phd' , 'phd') ,
        ('msr' , 'msr') ,
        ('ma' , 'ma') ,
)

class candidate(models.Model):
    start_time = models.CharField(max_length = 200 , blank = True)
    expected_time = models.CharField(max_length = 200 , blank = True)
    candidate_name = models.CharField(max_length = 200 , blank = False)
    company_name = models.CharField(max_length = 200 , blank = True)
    roll_number = models.CharField(max_length=50)
    is_selected = models.BooleanField(default = False)
    is_interview = models.BooleanField(default = False)

    def get_absolute_url(self):
        return reverse('homepage')
    def __str__(self):
        return self.candidate_name

class eligible(models.Model):
    cpi = models.CharField(max_length=100 , blank = True)
    major = models.CharField(max_length=100 , blank = True)
    minor = models.BooleanField(default=False , blank = True)
    programme = models.CharField(max_length = 100 , choices = programme)
    specialization = models.CharField(max_length=100 , blank = True)
    def __str__(self):
        return self.cpi

class company(models.Model):
    company_name = models.CharField(max_length = 200 , blank = False)
    cpoc = models.CharField(max_length = 200 , blank = False)
    cpoc_contact = models.CharField(max_length = 200 , blank = False)
    eligibility_criteria = models.ManyToManyField(eligible , related_name = 'eligible_companies' )
    waiting_candidate = models.ManyToManyField(candidate, related_name = 'waiting_person' , blank = True)
    shortlist_candidate = models.ManyToManyField(candidate, related_name = 'shortlist_person' , blank = True)
    all_candidate = models.ManyToManyField(candidate, related_name = 'all_person', blank = True)

    def __str__(self):
        return self.company_name

class poc (models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE , null=True)
    poc_id = models.CharField(max_length = 200 , blank = False)
    company = models.OneToOneField(company , on_delete=models.CASCADE, null=True)
    password = models.CharField(max_length = 200 , blank = False)
    def __str__(self):
        return self.poc_id

# class requirement( models.Model ):
    # poc_id = models.CharField

class announcement(models.Model):

    send_all = models.BooleanField(default=False , blank = True)
    poc = models.ForeignKey(poc, on_delete=models.CASCADE)
    description =  models.CharField(max_length = 200 , blank = False)

    def __str__(self):
        return self.poc.poc_id
