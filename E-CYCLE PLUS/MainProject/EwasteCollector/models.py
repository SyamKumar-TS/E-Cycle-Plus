from django.db import models

# Create your models here.

from django.utils import timezone

from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone

class CollectedEwaste(models.Model):
    collectedewaste_weight = models.FloatField(default=0)
    recyclable_weight = models.FloatField(default=0)
    nonrecyclable_weight = models.FloatField(default=0)
    rate_per_kg = models.FloatField(default=10)
    total_amount = models.FloatField(default=100)
    collectedewaste_date = models.DateField(default=timezone.now)
    
    # Use the correct app name 'admin' for the Yard model
    yard = models.ForeignKey('Admin.Yard', on_delete=models.CASCADE,null=True)
    
    # The Assignewastebooking model is in the EwasteCollector app
    Ewaste = models.ForeignKey('Admin.Assignewastebooking', on_delete=models.CASCADE)
    
    class Meta:
        db_table = "tbl_collectedewaste"