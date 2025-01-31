from django.db import models

class AcademicRecord(models.Model):
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year = models.IntegerField()
    score = models.FloatField()

class ResearchPaper(models.Model):
    title = models.CharField(max_length=255)
    authors = models.TextField()
    publication_date = models.DateField()
    journal = models.CharField(max_length=255) 