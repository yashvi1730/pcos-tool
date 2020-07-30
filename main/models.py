from django.db import models
# Create your models here.

class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=None,null=True,blank=True)
   
    email=models.EmailField()
    weight=models.CharField(max_length=5,default=None,null=True,blank=True)
    height_feet=models.CharField(max_length=5,default=None,null=True,blank=True)
    height_inches=models.CharField(max_length=5,default=None,null=True,blank=True)

class Medical_History(models.Model):
    pcos_medication=models.CharField(max_length=1000)
    other_medication=models.CharField(max_length=1000)
    allergies=models.CharField(max_length=1000)

class Schedule(models.Model):
    date=models.DateField()
    time=models.TimeField()




class Pcos_History(models.Model):
    pcos_diagnosed_age= models.CharField( max_length=128,default='less than 20')
    acne=models.CharField(max_length=100,default='not_correct',null=True,blank=True)
    excess_hair_growth=models.CharField(max_length=100,default='not_correct',null=True,blank=True)
    irr_period=models.CharField(max_length=100,default='not_correct',null=True,blank=True)
    weight_gain=models.CharField(max_length=100,default='not_correct',null=True,blank=True)
    hair_loss=models.CharField(max_length=100,default='not_correct',null=True,blank=True)
    diff_conceiving=models.CharField(max_length=100,default='not_correct',null=True,blank=True)
    poly_cystic_ovaries=models.CharField(max_length=100,default='not_correct',null=True,blank=True)
    other=models.CharField(max_length=100,default='not_correct',null=True,blank=True)
    none=models.CharField(max_length=100,default='not_correct',null=True,blank=True)
    lactation=models.CharField(max_length=100,default='appropriate',null=True,blank=True)
    skin_tag_armpit=models.CharField(max_length=100,default='not_there',null=True,blank=True)
    sleeping_disorder=models.CharField(max_length=100,default='not_there',null=True,blank=True)
    hypothyroidism=models.CharField(max_length=100,default='not_there',null=True,blank=True)
    sudden_hunger=models.CharField(max_length=100,default='not_there',null=True,blank=True)
    headaches=models.CharField(max_length=100,default='not_there',null=True,blank=True)
    sex_drive=models.CharField(max_length=100,default='normal',null=True,blank=True)
    feel_of_guilt=models.CharField(max_length=100,default='not_there',null=True,blank=True)


class Purpose_of_visit(models.Model):
    purpose=models.CharField(max_length=100)
    add_reason=models.CharField(max_length=1000)
    docfile = models.FileField(upload_to='documents/',default='none')
    


   
class Test(models.Model):
    t_name=models.CharField(max_length=100)
    t_age=models.IntegerField()


class Mensis(models.Model):
    m_age_first_period=models.CharField(max_length=5,blank=True,null=True,default='none')
    m_date_last_period=models.DateField()
    m_cycle_len=models.CharField(max_length=5,blank=True,null=True,default='none')
    m_period_len=models.CharField(max_length=5,blank=True,null=True,default='none')
    m_flow_amount=models.CharField(max_length=100,default='Medium')
    m_pain_scale=models.CharField(max_length=100,default='Medium')
    m_bleed=models.CharField(max_length=100,default='no')
   



    

    


