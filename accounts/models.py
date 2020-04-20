from django.db import models

# Create your models here.
class patient_data(models.Model):
    name = models.CharField(max_length = 100)
    ultrasound = models.ImageField(upload_to = 'ultrasound/')

    def __str__(self):
        return self.name

class ImageCollector(models.Model):
    name = models.CharField(max_length = 100)
    patient_img = models.FileField(upload_to = 'patient_data/')
    created_at = models.DateTimeField(auto_now_add = True)
    username = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.name