from django.db import models

# Create your models here.

class survey(models.Model):

    Name = models.CharField(max_length=20)

    Email = models.EmailField()

    Age = models.IntegerField()

    career=(
        ('student','STUDENT'),
        ('Frondend Developer','FRONT END DEVELOPER'),
        ('Backend Developer','BACKEND DEVELOPER'),
        ('Not to say ','NOT TO SAY'),
        ('Other','OTHER')
    )

    Careerchoice = models.CharField(max_length=18,choices=career,default='Not to say')

    experience = (

        ('Five','FIVE'),
        ('Four','FOUR'),
        ('Three','THREE'),
        ('Two','TWO'),
        ('One','ONE'),
        ('Zero','ZERO')

    )

    Experience = models.CharField(max_length=6,choices=experience,default='Zero')


    Feedback = models.TextField()