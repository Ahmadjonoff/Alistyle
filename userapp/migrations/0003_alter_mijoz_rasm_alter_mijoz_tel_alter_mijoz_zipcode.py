# Generated by Django 4.0.3 on 2022-03-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_manzil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mijoz',
            name='rasm',
            field=models.FileField(blank=True, null=True, upload_to='mijoz'),
        ),
        migrations.AlterField(
            model_name='mijoz',
            name='tel',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='mijoz',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
