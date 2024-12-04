from django.db import models



from django.db import models

class KopSotilganKitob(models.Model):
    nomi = models.CharField(max_length=100)
    mualif = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    asar = models.CharField(max_length=100)
    file = models.FileField(upload_to='books/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Fayl nomini avtomatik tarzda belgilash
        if self.file:
            self.book_name = self.file.name.split('/')[-1]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nomi}"

class kun_iqtibos(models.Model):
    nomi = models.CharField(max_length=100)




    def __str__(self):
        return f"{self.nomi}"



class Kitob(models.Model):
    nomi = models.CharField(max_length=100)
    mualif = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    asar = models.CharField(max_length=100)
    file = models.FileField(upload_to='books/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Fayl nomini avtomatik tarzda belgilash
        if self.file:
            self.book_name = self.file.name.split('/')[-1]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nomi}"
