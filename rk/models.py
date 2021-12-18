from django.db import models

class Orchestra(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_orchestra'

class Musician(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    orchestra_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_musicians'