from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from PIL import Image
import uuid
import os.path

def rename_image(instance, filename):
    path = "profil_foto"
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(str(uuid.uuid4())[:8], ext)

    return os.path.join(path, filename)

class Profil(models.Model):

    TYPE_CHOICES = (
        ('ADMIN', 'ADMIN'),
        ('MANAGER', 'MANAGER'),
        ('USER', 'USER'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil', blank=True, null=True)
    foto = models.ImageField(null=True, blank=True, upload_to=rename_image, default="profil_foto/6b9f250c.jpg",)
    user_type = models.CharField(max_length=255, choices=TYPE_CHOICES, default='USER')
    name = models.CharField(max_length=55, blank=True, null=True)
    surname = models.CharField(max_length=55, blank=True, null=True)

    objects = models.Manager()  # default manager

    def save(self, *args, **kwargs):
        ### IMAGE RESIZE
        super().save(*args, **kwargs)
        if self.foto:
            img = Image.open(self.foto.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.foto.path)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Profiller"


class Iha(models.Model):
	marka = models.CharField(max_length=55)
	model = models.CharField(max_length=55)
	agirlik = models.IntegerField()
	kategori = models.CharField(max_length=55)

	objects = models.Manager()  # default manager

	def __str__(self):
		return self.marka + "_" + self.model

	class Meta:
		verbose_name_plural = "İHA Listesi"
		verbose_name = "İHA"

class Kiralama(models.Model):
	iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
	uye = models.ForeignKey(User, on_delete=models.CASCADE)
	atarihi = models.DateField(blank=True, null=True)
	asaati = models.TimeField(blank=True, null=True)
	vtarihi = models.DateField(blank=True, null=True)
	vsaati = models.TimeField(blank=True, null=True)

	objects = models.Manager()  # default manager

	def __str__(self):
		return str(self.uye) + "_" + str(self.iha)

	class Meta:
		verbose_name_plural = "Kiralama Kayıtları"
		verbose_name = "Kiralama"