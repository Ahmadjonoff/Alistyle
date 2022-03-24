# Generated by Django 4.0.3 on 2022-03-16 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('jins', models.CharField(choices=[('Ayol', 'Ayol'), ('Erkak', 'Erkak')], max_length=10)),
                ('tel', models.CharField(max_length=13)),
                ('zipcode', models.CharField(max_length=10)),
                ('mamlakat', models.CharField(max_length=30)),
                ('shahar', models.CharField(max_length=30)),
                ('rasm', models.FileField(blank=True, upload_to='mijoz')),
                ('sana', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]