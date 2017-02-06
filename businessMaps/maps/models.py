from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TestEntry(models.Model):
	test_text=models.CharField(max_length=200)
	def __str__(self):
		return self.test_text