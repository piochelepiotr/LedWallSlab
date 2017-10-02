from django.db import models

# LedWall config model
class Configuration(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    config = models.TextField(null=True)
    creation = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Creation")
    modification = models.DateTimeField(auto_now_add=False, auto_now=True,
                                verbose_name="Modification")

    def __str__(self):
        return self.name