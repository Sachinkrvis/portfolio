from django.db import models
from django.core.exceptions import ValidationError
from core.fields import MyCloudinaryField

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = MyCloudinaryField('portfolio_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Allow only one Portfolio object
        if not self.pk and Portfolio.objects.exists():
            raise ValidationError("You can only have one Portfolio.")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="projects")
    project_name = models.CharField(max_length=200)
    project_des = models.TextField()
    project_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.project_name


class Certificate(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="certificates")
    certificate_name = models.CharField(max_length=200)
    certificate_des = models.TextField()
    certificate_link = models.URLField(max_length=200, blank=True, null=True)
    certificate_image = MyCloudinaryField('certificates/', blank=True, null=True)  # ✅ now handled by Cloudinary

    def __str__(self):
        return self.certificate_name



class Info(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="infos")
    leet_code = models.IntegerField()
    professional_exp = models.IntegerField()
    intern_ship = models.IntegerField()

    def save(self, *args, **kwargs):
        # Allow only one Info object
        if not self.pk and Info.objects.exists():
            raise ValidationError("You can only have one Info.")
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.leet_code)
    


