from django.db import models
import uuid

# Create your models here.
class result_store(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fever = models.BooleanField(default=False)
    sore_throat = models.BooleanField(default=False)
    shortness_of_breath = models.BooleanField(default=False)
    head_ache = models.BooleanField(default=False)
    age_60_and_above = models.BooleanField(default=False)
    corona_result = models.BooleanField(null=True)
    gender = models.IntegerField(default=0)
    testReason_Abroad = models.BooleanField(default=False)
    testReason_Other = models.BooleanField(default=False)
    testReason_Contact_with_confirmed = models.BooleanField(default=False)


    