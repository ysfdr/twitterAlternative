# Generated by Django 4.1.4 on 2023-03-20 06:25

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
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bdate', models.DateField(verbose_name='Doğum tarihi')),
                ('agree', models.BooleanField(null=True, verbose_name='Şart ve koşul onayı')),
                ('photo', models.ImageField(null=True, upload_to=None, verbose_name='Foto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
