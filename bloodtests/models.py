from django.db import models
from django.core.validators import MinValueValidator


class Test(models.Model):
    code = models.CharField(max_length=4, primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)

    lower = models.FloatField(validators=[MinValueValidator(0.0)], null=True)
    upper = models.FloatField(validators=[MinValueValidator(0.0)], null=True)

    def save(self, *args, **kwargs):
        self.lower = round(self.lower, 1) if self.lower else None
        self.upper = round(self.upper, 1) if self.upper else None
        super(Test, self).save(*args, **kwargs)
