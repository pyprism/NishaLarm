from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Api(models.Model):
	rater = models.ForeignKey(User)
	account_sid = models.CharField(max_length=50)
	auth_token = models.CharField(max_length=50)
	from_no = models.CharField(max_length=30)
	to_no = models.CharField(max_length=30)


class Nisha(models.Model):
	santo = models.ForeignKey(User)
	message = models.TextField(null=True, blank=True)
	time = models.DateTimeField()
	interval = models.DateTimeField()
