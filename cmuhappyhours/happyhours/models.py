from django.db import models

# Create your models here.

class Courses(models.Model):
	course_id = models.IntegerField(max_length=10, primary_key=True)
	course_name = models.CharField(max_length=150)

class TA(models.Model):
	u_id = models.AutoField(primary_key=True)
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	courseNum = models.IntegerField(max_length=10)

class OfficeHours(models.Model):
	o_id = models.AutoField(primary_key=True)
	ta_id = models.ForeignKey(TA)
	day = models.CharField(max_length=20)
	start_time = models.CharField(max_length=100)
	end_time = models.CharField(max_length=100)
	venue = models.CharField(max_length=200)