# Generated by Django 4.2.3 on 2023-07-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baykar', '0002_profil'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='name',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='surname',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
