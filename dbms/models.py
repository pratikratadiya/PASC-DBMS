from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class user(AbstractUser):
	event = models.CharField(max_length=50)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = "user"
		verbose_name_plural = "user"

class Participant(models.Model):
	receipt_no = models.IntegerField(unique=True)
	name = models.CharField(max_length=100)
	emailid = models.EmailField(max_length=254,blank=True)
	year = models.CharField(max_length=5)
	phno = models.CharField(max_length=15)

	def __str__(self):
		return str(self.receipt_no)

	class Meta:
		verbose_name = "Participant"
		verbose_name_plural = "Participant"

class Event(models.Model):
	event_name = models.CharField(max_length=50)
	cost = models.IntegerField(blank=True,default=50)

	def __str__(self):
		return self.event_name

	class Meta:
		verbose_name = "Event"
		verbose_name_plural = "Event"

class Slot_list(models.Model):
	slot_no = models.IntegerField(default=1)
	slot_timing = models.CharField(max_length=50)

	def __str__(self):
		return self.slot_timing

	class Meta:
		verbose_name = "Slot_List"
		verbose_name_plural = "Slot_List"	

class Registration(models.Model):
	receipt_no = models.ForeignKey(Participant,on_delete=models.CASCADE)
	reported = models.BooleanField(default=False)
	certificate = models.BooleanField(default=False)
	slot_no = models.ForeignKey(Slot_list,on_delete=models.CASCADE)
	is_team = models.BooleanField(default=False)
	event = models.ForeignKey(Event,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.receipt_no.receipt_no) + ":" + self.event.event_name

	class Meta:
		verbose_name = "Registration"
		verbose_name_plural = "Registration"